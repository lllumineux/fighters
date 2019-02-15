from BuildingLevels import Background, StativeTexture, stative_textures_sprites,\
	background_sprites


def building():
	global bonus_mas_pos
	global narkomany
	global background
	bonus_mas_pos = []
	fighters_mas_pos = []
	narkomany = False
	background = Background(background_sprites, 'perfecto.jpg')
	StativeTexture(stative_textures_sprites, (201, 178), (1719, 191))
	fighters_mas_pos.append((244, 56))
	fighters_mas_pos.append((1644, 52))
	StativeTexture(stative_textures_sprites, (1, 368), (825, 374))
	StativeTexture(stative_textures_sprites, (1083, 363), (1918, 370))
	StativeTexture(stative_textures_sprites, (86, 370), (0, 200))
	StativeTexture(stative_textures_sprites, (168, 368), (76, 283))
	StativeTexture(stative_textures_sprites, (1817, 210), (1919, 365))
	StativeTexture(stative_textures_sprites, (1753, 287), (1847, 365))
	bonus_mas_pos.append((943, 155))
	StativeTexture(stative_textures_sprites, (922, 383), (975, 563))
	StativeTexture(stative_textures_sprites, (888, 451), (1010, 560))
	StativeTexture(stative_textures_sprites, (556, 519), (1338, 553))
	StativeTexture(stative_textures_sprites, (622, 545), (474, 628))
	StativeTexture(stative_textures_sprites, (525, 621), (337, 708))
	StativeTexture(stative_textures_sprites, (1307, 542), (1450, 623))
	StativeTexture(stative_textures_sprites, (1394, 613), (1581, 693))
	StativeTexture(stative_textures_sprites, (4, 878), (1919, 911))
	StativeTexture(stative_textures_sprites, (327, 881), (243, 795))
	StativeTexture(stative_textures_sprites, (256, 883), (129, 722))
	StativeTexture(stative_textures_sprites, (165, 896), (52, 635))
	StativeTexture(stative_textures_sprites, (88, 890), (1, 586))
	StativeTexture(stative_textures_sprites, (174, 523), (240, 540))
	StativeTexture(stative_textures_sprites, (1647, 883), (1733, 786))
	StativeTexture(stative_textures_sprites, (1715, 891), (1791, 708))
	StativeTexture(stative_textures_sprites, (1770, 889), (1859, 627))
	StativeTexture(stative_textures_sprites, (1796, 887), (1918, 560))
	StativeTexture(stative_textures_sprites, (1699, 549), (1618, 535))
	StativeTexture(stative_textures_sprites, (192, 724), (133, 635))
	StativeTexture(stative_textures_sprites, (124, 635), (0, 566))
	bonus_mas_pos.append((939, 777))
	return bonus_mas_pos, narkomany, fighters_mas_pos
