from BuildingLevels import Background, StativeTexture, stative_textures_sprites,\
    background_sprites


def building():
    global bonus_mas_pos
    global narkomany
    global background
    bonus_mas_pos = []
    fighters_mas_pos = []
    narkomany = False
    background = Background(background_sprites, 'redline.jpg')
    StativeTexture(stative_textures_sprites, (111, 628), (282, 682))
    StativeTexture(stative_textures_sprites, (1751, 597), (1602, 645))
    fighters_mas_pos.append((176, 516))
    fighters_mas_pos.append((1667, 499))
    StativeTexture(stative_textures_sprites, (364, 606), (1490, 597))
    bonus_mas_pos.append((955, 549))
    return bonus_mas_pos, narkomany, fighters_mas_pos
