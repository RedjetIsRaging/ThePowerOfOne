import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, size: int):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill("grey")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift) -> None:
        self.rect.x += x_shift
