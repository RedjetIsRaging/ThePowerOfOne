import pygame, sys


def main():
    pygame.init()
    game_width = 1200
    game_height = 700
    screen = pygame.display.set_mode((game_width, game_height))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill("black")

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
