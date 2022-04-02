import pygame
from tiles import Tile, StaticTile, AnimatedTile
from enemy import Enemy
from settings import tile_size, game_width, player_speed
from player import Player
from utils import import_csv_layout, import_cut_graphics
from game_data import level_1
from clouds import Clouds


class Level:
    def __init__(self, level_data: list[str], surface):
        # Set up the level
        self.display_surface = surface
        # self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        # self.initialize_level(level_data)
        self.world_shift = -8
        # self.current_x = 0

        # Player
        player_layout = import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)

        self.sprites_group = []
        for item in level_1.keys():
            if item not in ['player', 'enemies', 'flower', 'constraints']:
                layout = import_csv_layout(level_data[item])
                self.sprites_group.append(self.create_tile_group(layout, item))

        # flowers
        flower_layout = import_csv_layout(level_data['flower'])
        self.sprites_group.append(self.create_tile_group(flower_layout, 'flower'))

        # Enemy
        enemy_layout = import_csv_layout(level_data['enemies'])
        self.enemy_sprites = self.create_tile_group(enemy_layout, 'enemies')

        # Enemy constraint
        constraint_layout = import_csv_layout(level_data['constraints'])
        self.constraint_sprites = self.create_tile_group(constraint_layout, 'constraints')

        # Clouds
        self.clouds = Clouds(400, game_width, 8)

    def create_tile_group(self, layout, tile_type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for column_index, val in enumerate(row):
                if val != '-1':
                    x = column_index * tile_size
                    y = row_index * tile_size

                    if tile_type not in ['player', 'enemies', 'flower', 'constraints']:
                        terrain_tile_list = import_cut_graphics('levels/level_1/graphics/outside_tileset.png')
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if tile_type == 'flower':
                        sprite = AnimatedTile(tile_size, x, y, 'levels/level_1/graphics/tiles/flower')
                        sprite.animation_speed = 0.03  # don't need our flowers spinning *that* fast, do we
                        sprite_group.add(sprite)

                    if tile_type == 'enemies':
                        sprite = Enemy(tile_size, x, y)
                        sprite.animation_speed = 0.08
                        sprite_group.add(sprite)

                    if tile_type == 'constraints':
                        sprite = Tile(tile_size, x, y)
                        sprite_group.add(sprite)

        return sprite_group

    def player_setup(self, layout):
        for row_index, row in enumerate(layout):
            for column_index, val in enumerate(row):
                x = column_index * tile_size
                y = row_index * tile_size
                if val == '0':
                    print("player goes here")
                if val == '1':
                    end_surface = pygame.image.load('levels/universal/player.png').convert_alpha()
                    sprite = StaticTile(tile_size, x, y, end_surface)
                    self.goal.add(sprite)

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
            self.world_shift = player_speed
            player.speed = 0
        elif player_x > game_width / 2 and direction_x > 0:
            self.world_shift = -player_speed
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = player_speed

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right

        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        elif player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.on_ceiling = True

                player.direction.y = 0

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    def enemy_collision_reverse(self):
        for enemy in self.enemy_sprites.sprites():
            if pygame.sprite.spritecollide(enemy, self.constraint_sprites, False):
                enemy.reverse()

    def draw_level(self) -> None:
        self.clouds.draw(self.display_surface, self.world_shift)

        for sprite_group in self.sprites_group:
            sprite_group.update(self.world_shift)
            sprite_group.draw(self.display_surface)

        self.enemy_sprites.draw(self.display_surface)
        self.enemy_sprites.update(self.world_shift)
        self.enemy_collision_reverse()
        self.constraint_sprites.update(self.world_shift)  # Don't want to display the enemy constraints

        self.goal.update(self.world_shift)
        self.goal.draw(self.display_surface)


        # Render level tiles
        # self.tiles.update(self.world_shift)
        # self.tiles.draw(self.display_surface)
        # self.scroll_x()
        #
        # # Render player
        # self.player.update()
        # self.horizontal_movement_collision()
        # self.vertical_movement_collision()
        # self.player.draw(self.display_surface)
