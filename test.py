import pygame, sys

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, pic_path):
        super().__init__()
        self.image = pygame.image.load(pic_path)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

pygame.init()
clock = pygame.time.Clock()

screen_width = 820
screen_height = 462
screen = pygame.display.set_mode((screen_width, screen_height))
backgroud = pygame.image.load("mountain.png")
pygame.mouse.set_visible(False)


crosshair = Crosshair("circle-03.png")

crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        screen.blit(backgroud, (0, 0))
        crosshair_group.draw(screen)
        crosshair_group.update()
        clock.tick(80)

