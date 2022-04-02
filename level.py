import pygame
from tiles import Tile
from settings import tile_size, game_width
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

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < game_width / 3 and direction_x < 0:
            self.world_shift = 5
            player.speed = 0
        elif player_x > game_width / 2 and direction_x > 0:
            self.world_shift = -5
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 5

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom

                player.direction.y = 0

    def draw_level(self) -> None:
        # Render level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        # Render player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
