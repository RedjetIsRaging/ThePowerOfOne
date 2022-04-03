# a 2d list representation of the level
# X's are tiles, P is the starting position of the player
# level_map = [
#     '                             ',
#     '                             ',
#     '                   ####     ',
#     ' XX   XXX         #  ###     ',
#     ' XX P             #######    ',
#     ' XXXX             #######    ',
#     ' XXXX             ##  ##    ',
#     ' XX      X XXXX     XX   XXX ',
#     '         X XXXX     XX   XXX ',
#     '                    XX  XXXX ',
#     'XXXXXXXXXXXXXXXXXX  XX  XXXX '
# ]

# Level settings
vertical_tile_count = 11
tile_size = 64
game_width = 1200
game_height = vertical_tile_count * tile_size

# Player settings
player_speed = 8
