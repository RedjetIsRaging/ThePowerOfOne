import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, size: int, x: int, y: int) -> None:
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, x_shift) -> None:
        self.rect.x += x_shift


class StaticTile(Tile):
    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y)
        self.image = surface