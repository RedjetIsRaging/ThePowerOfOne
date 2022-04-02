# a 2d list representation of the level
# X's are tiles, P is the starting position of the player
level_map = [
    '                             ',
    '                             ',
    '                             ',
    ' XX   XXX            XX      ',
    ' XX P                        ',
    ' XXXX          XX      XX    ',
    ' XXXX        XX          XX  ',
    ' XX      X XXXX     XX   XXX ',
    '         X XXXX     XX   XXX ',
    '                    XX  XXXX ',
    'XXXXXXXXXXXXXXXXXX  XX  XXXX '
]

tile_size = 64
game_width = 1200
game_height = len(level_map) * tile_size
