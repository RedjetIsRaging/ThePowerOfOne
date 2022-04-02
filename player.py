import pygame
from utils import import_folder
from settings import player_speed


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.animations = {"idle": [], "schmoov": [] , "jump": [], "fall": []}
        self.import_character_assets()

        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations["idle"][self.frame_index]

        self.rect = self.image.get_rect(topleft=pos)

        # Movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = player_speed
        self.gravity = 0.8
        self.jump_speed = -16

        # Status
        self.status = "idle"
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

    def import_character_assets(self):
        base_path = "assets/character/"

        for animation in self.animations.keys():
            full_path = base_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        used_sprite = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = used_sprite
        else:
            flipped_sprite = pygame.transform.flip(used_sprite, True, False)
            self.image = flipped_sprite

        # Adjust hit box
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright=self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP] and self.on_ground:
            self.jump()

    def get_status(self):
        if self.direction.y < 0 and not self.on_ground:
            self.status = "jump"
        elif self.direction.y > 1 and not self.on_ground:
            self.status = "fall"
        else:
            if self.direction.x != 0 and self.on_ground:
                self.status = "schmoov"
            elif self.direction.x == 0 and self.on_ground:
                self.status = "idle"

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()
