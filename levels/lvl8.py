from BuildingLevels import Background, StativeTexture, stative_textures_sprites,\
    background_sprites
 
 
def building():
    global bonus_mas_pos
    global narkomany
    global background
    bonus_mas_pos = []
    fighters_mas_pos = []
    narkomany = False
    background = Background(background_sprites, 'windows.png')
    StativeTexture(stative_textures_sprites, (1704, 711), (1918, 734))
    StativeTexture(stative_textures_sprites, (1704, 711), (1763, 1042))
    StativeTexture(stative_textures_sprites, (1679, 565), (1919, 589))
    StativeTexture(stative_textures_sprites, (1681, 589), (1626, 329))
    StativeTexture(stative_textures_sprites, (1626, 329), (1919, 284))
    StativeTexture(stative_textures_sprites, (0, 860), (146, 899))
    StativeTexture(stative_textures_sprites, (146, 863), (104, 1042))
    StativeTexture(stative_textures_sprites, (226, 973), (514, 1001))
    StativeTexture(stative_textures_sprites, (614, 974), (824, 998))
    StativeTexture(stative_textures_sprites, (946, 974), (1133, 997))
    StativeTexture(stative_textures_sprites, (1225, 971), (1371, 1004))
    StativeTexture(stative_textures_sprites, (1474, 974), (1603, 1001))
    StativeTexture(stative_textures_sprites, (0, 717), (172, 727))
    StativeTexture(stative_textures_sprites, (172, 721), (167, 313))
    StativeTexture(stative_textures_sprites, (168, 313), (1, 324))
    bonus_mas_pos.append((22, 821))
    bonus_mas_pos.append((1888, 671))
    StativeTexture(stative_textures_sprites, (1545, 983), (1596, 904))
    StativeTexture(stative_textures_sprites, (1628, 855), (1689, 903))
    fighters_mas_pos.append((68, 761))
    fighters_mas_pos.append((1788, 629))
    StativeTexture(stative_textures_sprites, (132, 906), (236, 970))
    StativeTexture(stative_textures_sprites, (1652, 855), (1737, 814))
    StativeTexture(stative_textures_sprites, (1708, 782), (1679, 818))
    StativeTexture(stative_textures_sprites, (1705, 763), (1697, 786))
    StativeTexture(stative_textures_sprites, (0, 227), (173, 234))
    StativeTexture(stative_textures_sprites, (173, 230), (153, 0))
    StativeTexture(stative_textures_sprites, (1740, 2), (1732, 173))
    StativeTexture(stative_textures_sprites, (1733, 174), (1918, 169))
    StativeTexture(stative_textures_sprites, (1280, 487), (1378, 491))
    StativeTexture(stative_textures_sprites, (1380, 491), (1363, 392))
    StativeTexture(stative_textures_sprites, (1379, 391), (1279, 408))
    StativeTexture(stative_textures_sprites, (1280, 408), (1289, 489))
    StativeTexture(stative_textures_sprites, (300, 845), (494, 864))
    StativeTexture(stative_textures_sprites, (566, 805), (730, 829))
    StativeTexture(stative_textures_sprites, (774, 741), (919, 764))
    StativeTexture(stative_textures_sprites, (978, 689), (1145, 709))
    StativeTexture(stative_textures_sprites, (1211, 656), (1363, 684))
    StativeTexture(stative_textures_sprites, (1427, 659), (1521, 688))
    StativeTexture(stative_textures_sprites, (1557, 700), (1613, 719))
    bonus_mas_pos.append((1245, 628))
    return bonus_mas_pos, narkomany, fighters_mas_pos
