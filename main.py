import pygame
import sys
from settings import *
from level import Level


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((game_width, game_height))
    clock = pygame.time.Clock()
    level = Level(level_map, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill("black")
        level.draw_level()

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
