import pygame
from csv import reader
from os import walk
from settings import tile_size


def import_folder(path: str) -> list[str]:
    surface_list = []

    for _, __, img_files in walk(path):
        for img in img_files:
            full_path = path + "/" + img
            image_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)
    return surface_list


def import_csv_layout(path: str) -> list[list[str]]:
    terrain_map = []
    with open(path) as level_map:
        level = reader(level_map, delimiter=',')
        for row in level:
            terrain_map.append(list(row))

    return terrain_map


def import_cut_graphics(path: str) -> list[pygame.Surface]:
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_size()[0] / tile_size)
    tile_num_y = int(surface.get_size()[1] / tile_size)

    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * tile_size
            y = row * tile_size
            new_surface = pygame.Surface((tile_size, tile_size))
            new_surface.blit(surface, (0, 0), pygame.Rect(x, y, tile_size, tile_size))
            cut_tiles.append(new_surface)

    return cut_tiles
