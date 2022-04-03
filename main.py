import pygame
import sys
from settings import *
from level import Level
from game_data import level_1_files
from overworld import Overworld


def main() -> None:
    class Game:
        def __init__(self):
            self.max_level: int = 3
            self.overworld: Overworld = Overworld(0, self.max_level, screen)

        def run(self):
            self.overworld.run()

    pygame.init()
    engage_brand()  # Add window icon, set window title

    screen = pygame.display.set_mode((game_width, game_height))
    clock = pygame.time.Clock()
    game = Game()

    # address this level = Level(level_1_files, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill('black')
        game.run()
        # address this level.draw_level()

        pygame.display.update()
        clock.tick(60)


def engage_brand():
    pygame.display.set_caption("The power of one!")
    icon = pygame.image.load("assets/icon.png")
    pygame.display.set_icon(icon)


if __name__ == '__main__':
    main()
