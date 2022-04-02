import pygame
import sys
from settings import *
from level import Level
from game_data import level_1


def main() -> None:
    pygame.init()
    pygame.display.set_caption("The power of one!")
    icon = pygame.image.load("assets/icon.png")
    pygame.display.set_icon(icon)

    screen = pygame.display.set_mode((game_width, game_height))
    clock = pygame.time.Clock()

    level = Level(level_1, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill('cyan')
        level.draw_level()

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
