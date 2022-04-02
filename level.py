import pygame
from tiles import Tile
from settings import tile_size
from player import Player


class Level:
    def __init__(self, level_data: list[str], surface):
        # Set up the level
        self.display_surface = surface
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.initialize_level(level_data)
        self.world_shift = 0


    def initialize_level(self, layout) -> None:
        for row_index, row in enumerate(layout):
            for col_index, tile in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if tile == "X":
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                elif tile == "P":
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def draw_level(self) -> None:
        # Render level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        # Render player
        self.player.update()
        self.player.draw(self.display_surface)
