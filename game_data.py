from settings import game_height

level_1_base_path = "assets/levels/level_1/level/"
level_1 = {
    'terrain': level_1_base_path + 'level_1_outside_terrain.csv',
    'grass': level_1_base_path + 'level_1_grass.csv',
    'sky': level_1_base_path + 'level_1_sky.csv',
    'tree': level_1_base_path + 'level_1_trees.csv',
    'house': level_1_base_path + 'level_1_house.csv',
    'flower': level_1_base_path + 'level_1_flowers.csv',
    'enemies': level_1_base_path + 'level_1_enemy.csv',
    'constraints': level_1_base_path + 'level_1_constraints.csv',
    'player': level_1_base_path + 'level_1_player.csv',
    'tile_set': 'assets/levels/level_1/graphics/outside_tileset.png',
    'enemy_sprites': 'assets/enemies/snake',
    'node_pos': (150, game_height / 2),
    'background_color': 'cyan',
    'clouds': True,
    'unlock': 1
}

level_2 = {
    'terrain': 'assets/levels/level_2/level/level_2_terrain.csv',
    'rocks': 'assets/levels/level_2/level/level_2_rock.csv',
    'cracks': 'assets/levels/level_2/level/level_2_cracks.csv',
    'enemies': 'assets/levels/level_2/level/level_2_enemy.csv',
    'constraints': 'assets/levels/level_2/level/level_2_constraint.csv',
    'player': 'assets/levels/level_2/level/level_2_player.csv',
    'enemy_sprites': 'assets/enemies/snail',
    'background_color': '#482223',
    'tile_set': 'assets/levels/level_2/graphics/rock_tileset.png',
    'node_pos': (405, (game_height / 2)),
    'clouds': False,
    'unlock': 2
}

level_3 = {
    'terrain': 'assets/levels/level_3/level/level_3_terrain.csv',
    'constraints': 'assets/levels/level_3/level/level_3_constraints.csv',
    'enemies': 'assets/levels/level_3/level/level_3_enemy.csv',
    'rocks': 'assets/levels/level_3/level/level_3_rocks.csv',
    'player': 'assets/levels/level_3/level/level_3_player.csv',
    'enemy_sprites': 'assets/enemies/guy',
    'background_color': '#4F507B',
    'tile_set': 'assets/levels/level_3/graphics/iceleset.png',
    'node_pos': (705, (game_height / 2)),
    'clouds': False,
    'unlock': 3
}
level_4 = {
    'decoration': 'assets/levels/level_4/level/level_4_decoration.csv',
    'terrain': 'assets/levels/level_4/level/level_4_terrain.csv',
    'player': 'assets/levels/level_4/level/level_4_player.csv',
    'tile_set': 'assets/levels/level_4/graphics/rainbow.png',
    'node_pos': (1050, (game_height / 2)),
    'background_color': 'black',
    'clouds': False,
    'unlock': 2
}


levels = {
    0: level_1,
    1: level_2,
    2: level_3,
    3: level_4
}
