#!/usr/bin/env python

import pygame
import numpy as np
import cProfile as profile
import timeit


pygame.init()
flags = pygame.DOUBLEBUF
screen = pygame.display.set_mode((500,500), flags)
screen.set_alpha(None)

def main(nrows, ncols):
    run = True
    grid = make_grid(nrows, ncols)
    print(grid)
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        screen.fill((0, 0, 0))
        active_rects = draw_grid(5, 5, 500, 500)
        active_rect = pygame.draw.rect(screen, (255,255, 255), (50, 50, 100, 20))
        active_rects.append(active_rect)
        # pygame.display.update(active_rects)
        pygame.display.flip()
        break
    print(active_rects, active_rect)
    pygame.quit()

def make_grid(nrows, ncols):
    grid = np.zeros((nrows, ncols))
    for row in range(nrows):
        for col in range(ncols):
            grid[row, col] = 2
            print(row, col)
    return grid


def draw_grid(nrows, ncols, width, height):
    row_gap = width // nrows
    col_gap= height // ncols
    active_rectangles = []
    for row in range(nrows):
        row_rect = pygame.draw.line(screen, (155, 155, 155), (0, row * row_gap), (width, row * row_gap))
        active_rectangles.append(row_rect)

    for col in range(ncols):
        col_rect = pygame.draw.line(screen, (155, 155, 155), (col * col_gap, 0), (col * col_gap, height))   
        active_rectangles.append(col_rect)
    return active_rectangles

if __name__ == "__main__":
    start = timeit.default_timer()
    main(40, 40)
    stop = timeit.default_timer()
    print("\n Time consumed: ", stop - start)
