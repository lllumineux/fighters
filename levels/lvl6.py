from BuildingLevels import Background, StativeTexture, stative_textures_sprites, background_sprites


def building():
    global bonus_mas_pos
    global narkomany
    global background
    bonus_mas_pos = []
    fighters_mas_pos = []
    narkomany = False
    background = Background(background_sprites, 'storm.jpg')
    StativeTexture(stative_textures_sprites, (0, 1012), (1905, 1049))
    StativeTexture(stative_textures_sprites, (1895, 1017), (1916, 1049))
    StativeTexture(stative_textures_sprites, (1898, 1013), (1916, 1049))
    StativeTexture(stative_textures_sprites, (254, 1005), (427, 955))
    StativeTexture(stative_textures_sprites, (254, 1003), (403, 1038))
    StativeTexture(stative_textures_sprites, (427, 1004), (397, 1027))
    fighters_mas_pos.append((129, 909))
    StativeTexture(stative_textures_sprites, (490, 889), (621, 910))
    StativeTexture(stative_textures_sprites, (636, 814), (689, 877))
    StativeTexture(stative_textures_sprites, (706, 773), (1396, 782))
    StativeTexture(stative_textures_sprites, (1407, 793), (1496, 856))
    StativeTexture(stative_textures_sprites, (1509, 865), (1582, 889))
    StativeTexture(stative_textures_sprites, (1645, 924), (1724, 1021))
    StativeTexture(stative_textures_sprites, (1741, 975), (1770, 1016))
    bonus_mas_pos.append((684, 976))
    bonus_mas_pos.append((1285, 980))
    bonus_mas_pos.append((815, 663))
    bonus_mas_pos.append((1264, 674))
    fighters_mas_pos.append((1797, 907))
    return bonus_mas_pos, narkomany, fighters_mas_pos
