from BuildingLevels import Background, StativeTexture, stative_textures_sprites, background_sprites


def building():
    global bonus_mas_pos
    global narkomany
    global background
    bonus_mas_pos = []
    fighters_mas_pos = []
    narkomany = False
    background = Background(background_sprites, 'flash.jpg')
    StativeTexture(stative_textures_sprites, (8, 799), (1852, 936))
    StativeTexture(stative_textures_sprites, (12, 805), (143, 28))
    StativeTexture(stative_textures_sprites, (1851, 28), (1775, 810))
    StativeTexture(stative_textures_sprites, (370, 802), (537, 698))
    StativeTexture(stative_textures_sprites, (1546, 797), (1365, 701))
    StativeTexture(stative_textures_sprites, (137, 595), (289, 635))
    StativeTexture(stative_textures_sprites, (1774, 627), (1621, 665))
    StativeTexture(stative_textures_sprites, (488, 513), (648, 552))
    StativeTexture(stative_textures_sprites, (1350, 525), (1547, 568))
    StativeTexture(stative_textures_sprites, (875, 800), (967, 587))
    StativeTexture(stative_textures_sprites, (874, 672), (761, 806))
    StativeTexture(stative_textures_sprites, (672, 803), (760, 734))
    StativeTexture(stative_textures_sprites, (965, 672), (1086, 813))
    StativeTexture(stative_textures_sprites, (1083, 722), (1179, 810))
    StativeTexture(stative_textures_sprites, (885, 677), (846, 772))
    StativeTexture(stative_textures_sprites, (751, 737), (917, 826))
    StativeTexture(stative_textures_sprites, (281, 81), (515, 211))
    StativeTexture(stative_textures_sprites, (1310, 107), (1697, 228))
    StativeTexture(stative_textures_sprites, (754, 251), (1144, 372))
    fighters_mas_pos.append((400, 100))
    fighters_mas_pos.append((1700, 100))
    return bonus_mas_pos, narkomany, fighters_mas_pos
