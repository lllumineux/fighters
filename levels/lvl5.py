from BuildingLevels import Background, StativeTexture, stative_textures_sprites,\
    background_sprites


def building():
    global bonus_mas_pos
    global narkomany
    global background
    bonus_mas_pos = []
    fighters_mas_pos = []
    narkomany = False
    background = Background(background_sprites, 'redone.jpg')
    StativeTexture(stative_textures_sprites, (5, 1016), (770, 1048))
    StativeTexture(stative_textures_sprites, (1230, 1014), (1917, 1049))
    StativeTexture(stative_textures_sprites, (797, 958), (963, 978))
    StativeTexture(stative_textures_sprites, (1080, 962), (1213, 985))
    fighters_mas_pos.append((53, 932))
    fighters_mas_pos.append((1776, 930))
    StativeTexture(stative_textures_sprites, (5, 899), (714, 913))
    StativeTexture(stative_textures_sprites, (1914, 897), (1308, 915))
    StativeTexture(stative_textures_sprites, (212, 904), (360, 831))
    StativeTexture(stative_textures_sprites, (1519, 900), (1690, 836))
    bonus_mas_pos.append((1879, 858))
    bonus_mas_pos.append((34, 864))
    StativeTexture(stative_textures_sprites, (459, 786), (642, 810))
    StativeTexture(stative_textures_sprites, (1300, 750), (1400, 780))
    StativeTexture(stative_textures_sprites, (691, 732), (761, 767))
    StativeTexture(stative_textures_sprites, (1193, 733), (1262, 772))
    StativeTexture(stative_textures_sprites, (804, 685), (868, 723))
    StativeTexture(stative_textures_sprites, (1099, 693), (1163, 724))
    StativeTexture(stative_textures_sprites, (955, 664), (1028, 682))
    bonus_mas_pos.append((986, 645))
    return bonus_mas_pos, narkomany, fighters_mas_pos
