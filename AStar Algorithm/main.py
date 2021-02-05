#!/usr/bin/env python3
import numpy as np
import pygame
from queue import PriorityQueue
import easygui
from time import sleep

pygame.init()

WIDTH = 680
HEIGHT = 680

# load images
logo_icon = pygame.image.load("image/path.png")
start_icon = pygame.image.load("image/start.png")
goal_icon = pygame.image.load("image/flag.png")
bg = pygame.image.load("image/bg1.jpg")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

clock = pygame.time.Clock()
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
pygame.display.set_caption("AStar Visualizer (2021)")
pygame.display.set_icon(logo_icon)
window.set_alpha(None)

LIGHT_BLUE = (75, 180, 250)
BLUE = (45, 124, 250)
WHITE = (255, 255, 255)
BLACK = (60, 60, 60)
YELLOW = (255, 250, 0)
GREY = (224, 224, 224)

class Cursor(pygame.sprite.Sprite):
    def __init__(self, pic):
        super().__init__()
        self.image = pygame.image.load(pic)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

start_cus = Cursor("image/start.png")
start_group = pygame.sprite.Group()
start_group.add(start_cus)

class Node:
    def __init__(self, row, col, node_width, node_height, total_rows, total_cols):
        self.row = row
        self.col = col
        self.x = col * node_width
        self.y = row * node_height
        self.color = WHITE  # white as a blank space
        self.width = node_width
        self.height = node_height
        self.neighbors = []
        self.total_rows = total_rows
        self.total_cols = total_cols

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == LIGHT_BLUE

    def is_barrier(self):
        return self.color == BLACK

    def is_open(self):
        return self.color == BLUE

    def is_start(self):
        return self.color == RED

    def is_end(self):
        return self.color == PURPLE

    def is_free(self):
        return self.color == WHITE

    def reset(self):
        self.color = WHITE
        self.draw_node()
        self.draw_frame()

    def make_closed(self):
        self.color = LIGHT_BLUE
        self.draw_node()
        self.draw_frame()

    def make_open(self):
        self.color = BLUE
        self.draw_node()
        self.draw_frame()

    def make_barrier(self):
        self.color = BLACK
        self.draw_node()

    def make_start(self):
        self.draw_icon(start_icon)

    def make_end(self):
        self.draw_icon(goal_icon)

    def make_path(self):
        self.color = YELLOW
        self.draw_node()

    def update_neighbors(self, grid):
        if self.row < self.total_rows - 1 and not grid[self.row+1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row-1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])

    def draw_node(self):
        active_node = pygame.draw.rect(
            window, self.color, (self.x, self.y, self.width, self.height), border_radius=1)
        pygame.display.update(active_node)

    def draw_icon(self, image):
        active_rect = pygame.draw.rect(
            window, GREY, (self.x + 1, self.y + 1, self.width - 1, self.height - 1), border_radius=1)
        pygame.Surface.blit(window, image, (self.x, self.y))
        pygame.display.update(active_rect)

    def draw_frame(self):
        active_rect = pygame.draw.rect(
            window, GREY, (self.x, self.y, self.width + 1, self.height + 1), width=1)
        pygame.display.update((active_rect))

    def draw_open(self):
        active_open = pygame.draw.rect(
            window, self.color, (self.x + 1, self.y + 1, self.width - 1, self.height - 1), border_radius=5)
        pygame.display.update(active_open)


# make a numpy array (grid) to store nodes
def make_grid(rows, cols, width, height):
    grid = np.zeros((rows, cols), dtype=object)
    row_gap = height // rows
    col_gap = width // cols

    for row in range(rows):
        for col in range(cols):
            grid[row][col] = Node(row, col, col_gap, row_gap, rows, cols)

    return grid


# draw the grey line grid onto the surface
def draw_grid(rows, cols, width, height):
    row_gap = width // rows
    col_gap = height // cols
    active_rectangles = []

    for row in range(rows):
        row_rect = pygame.draw.line(
            window, GREY, (0, row * row_gap), (width, row * row_gap))
        active_rectangles.append(row_rect)

    for col in range(cols):
        col_rect = pygame.draw.line(
            window, GREY, (col * col_gap, 0), (col * col_gap, height))
        active_rectangles.append(col_rect)

    return active_rectangles


# change mouse postion into specific (row, col) in the pygame window
def get_clicked_pos(pos, rows, cols, width, height):
    row_gap = height // rows
    col_gap = height // cols
    x, y = pos
    row = y // row_gap
    col = x // col_gap

    return row, col


# find heuristic distance
def heuristic(node1, node2):
    (x1, y1) = node1
    (x2, y2) = node2
    # use Manhattan distance
    return abs(x2-x1) + abs(y2-y1)
    # use Euclidean distance
    return np.sqrt(np.square(x2-x1) + np.square(y2-y2))


# reconstruction of path and path length
def reconstruct_path(came_from, current, path_length):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        sleep(0.03)

    return path_length


def astar(start, goal, grid):
    count = 0
    open_set = PriorityQueue()
    open_set_hash = {start}
    open_set.put((0, count, start))
    came_from = {}
    path_length = 0

    g_score = {node: float("inf") for row in grid for node in row}
    f_score = {node: float("inf") for row in grid for node in row}

    g_score[start] = 0
    f_score[start] = heuristic(start.get_pos(), goal.get_pos())

    while not open_set.empty():
        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == goal:
            goal.make_end()
            path_length = reconstruct_path(came_from, current, path_length)
            goal.make_end()
            start.make_start()
            return path_length

        for neighbor in current.neighbors:
            tentative_gscore = g_score[current] + 1
            if tentative_gscore < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_gscore
                f_score[neighbor] = tentative_gscore + \
                    heuristic(neighbor.get_pos(), goal.get_pos())
                path_length = g_score[neighbor]

                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        if current != start:
            current.make_closed()
        sleep(0.00005)

    return False


def main(width, height, num_rows, num_cols):
    run = True
    start = None
    end = None
    # window.fill(WHITE)
    pygame.Surface.blit(window, bg, (0,0))
    draw_grid(num_rows, num_cols, WIDTH, HEIGHT)
    pygame.display.flip()
    grid = make_grid(num_rows, num_cols, width, height)

    
    while run:
        start_group.draw(window)
        start_group.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(
                    pos, num_rows, num_cols, WIDTH, HEIGHT)
                node = grid[row, col]
                if not start and node != end:
                    start = node
                    start.make_start()

                elif not end and node != start:
                    end = node
                    end.make_end()
                elif node != end and node != start and not node.is_barrier():
                    node.make_barrier()

            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(
                    pos, num_rows, num_cols, WIDTH, HEIGHT)
                node = grid[row, col]
                if not node.is_free():
                    node.reset()
                    if node == start:
                        start = None
                        print("reset start point")

                    elif node == end:
                        end = None
                        print("reset goal point")

                    else:
                        print("reset badrrier")

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    break

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    pygame.Surface.blit(window, bg, (0, 0))
                    grid = make_grid(num_rows, num_cols, width, height)
                    draw_grid(num_rows, num_cols, WIDTH, HEIGHT)
                    pygame.display.flip()

                if(event.key == pygame.K_SPACE or event.key == pygame.K_RETURN) and start != None and end != None:

                    for row in range(grid.shape[0]):
                        for col in range(grid.shape[1]):
                            grid[row][col].update_neighbors(grid)

                    path_length = astar(start, end, grid)
                    if path_length:
                        print("Astar successfully finished")
                        print("Path Length: {length}".format(length = path_length))
                        easygui.msgbox(msg ="Path Length: {path_length}".format(path_length = path_length), title="AStar Path Finder", image="image/success.png")

                    else:
                        print("Failed to find the path")
                        easygui.msgbox("Failed to find the path.", title = "AStar Path Finder", image = "image/fail.png")
                        
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main(WIDTH, HEIGHT, 40, 40)
