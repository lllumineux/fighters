from BuildingLevels import Background, StativeTexture, stative_textures_sprites,\
    background_sprites


def building():
    global bonus_mas_pos
    global narkomany
    global background
    bonus_mas_pos = []
    fighters_mas_pos = []
    narkomany = False
    background = Background(background_sprites, 'flash.jpg')
    StativeTexture(stative_textures_sprites, (4, 973), (1918, 1018))
    fighters_mas_pos.append((7, 863))
    fighters_mas_pos.append((1866, 869))
    StativeTexture(stative_textures_sprites, (105, 890), (184, 980))
    StativeTexture(stative_textures_sprites, (176, 813), (263, 982))
    StativeTexture(stative_textures_sprites, (1708, 891), (1800, 974))
    StativeTexture(stative_textures_sprites, (1720, 978), (1622, 810))
    StativeTexture(stative_textures_sprites, (388, 813), (1484, 831))
    StativeTexture(stative_textures_sprites, (917, 813), (985, 726))
    bonus_mas_pos.append((942, 706))
    StativeTexture(stative_textures_sprites, (255, 891), (322, 973))
    StativeTexture(stative_textures_sprites, (1624, 893), (1555, 976))
    StativeTexture(stative_textures_sprites, (1045, 686), (1395, 714))
    StativeTexture(stative_textures_sprites, (859, 708), (478, 685))
    return bonus_mas_pos, narkomany, fighters_mas_pos
