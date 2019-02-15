from BuildingLevels import Background, StativeTexture, stative_textures_sprites, background_sprites


def building():
    global bonus_mas_pos
    global narkomany
    global background
    bonus_mas_pos = []
    fighters_mas_pos = []
    narkomany = False
    background = Background(background_sprites, 'lave.jpg')
    StativeTexture(stative_textures_sprites, (0, 1004), (1919, 1034))
    fighters_mas_pos.append((113, 900))
    fighters_mas_pos.append((1794, 918))
    StativeTexture(stative_textures_sprites, (372, 1013), (529, 925))
    StativeTexture(stative_textures_sprites, (1473, 1008), (1544, 916))
    StativeTexture(stative_textures_sprites, (571, 830), (689, 899))
    StativeTexture(stative_textures_sprites, (743, 776), (796, 807))
    StativeTexture(stative_textures_sprites, (1346, 826), (1455, 906))
    StativeTexture(stative_textures_sprites, (1243, 748), (1327, 814))
    StativeTexture(stative_textures_sprites, (700, 761), (829, 814))
    StativeTexture(stative_textures_sprites, (1118, 672), (1227, 747))
    StativeTexture(stative_textures_sprites, (862, 699), (919, 737))
    StativeTexture(stative_textures_sprites, (993, 625), (1056, 668))
    StativeTexture(stative_textures_sprites, (934, 675), (982, 696))
    bonus_mas_pos.append((1027, 599))
    StativeTexture(stative_textures_sprites, (993, 665), (1052, 1010))
    StativeTexture(stative_textures_sprites, (1055, 666), (1035, 1009))
    StativeTexture(stative_textures_sprites, (1056, 668), (1026, 1011))
    StativeTexture(stative_textures_sprites, (6, 623), (807, 661))
    StativeTexture(stative_textures_sprites, (1308, 643), (1900, 627))
    return bonus_mas_pos, narkomany, fighters_mas_pos
