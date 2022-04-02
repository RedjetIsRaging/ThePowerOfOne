import pygame
from tiles import Tile
from settings import tile_size


class Level:
    def __init__(self, level_data: list[str], surface):
        # Set up the level
        self.display_surface = surface
        self.tiles = pygame.sprite.Group()
        self.initialize_level(level_data)
        self.world_shift = 0

    def initialize_level(self, layout) -> None:
        for row_index, row in enumerate(layout):
            for col_index, tile in enumerate(row):
                if tile == "X":
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)

    def draw_level(self) -> None:
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
