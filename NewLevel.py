from BuildingLevels import Background, StativeTexture, stative_textures_sprites,\
	background_sprites


def building():
	global bonus_mas_pos
	global narkomany
	global background
	bonus_mas_pos = []
	fighters_mas_pos = []
	narkomany = False
	background = Background(background_sprites, 'white.png')
	StativeTexture(stative_textures_sprites, (1, 851), (827, 939))
	StativeTexture(stative_textures_sprites, (1087, 845), (1916, 938))
	StativeTexture(stative_textures_sprites, (928, 826), (989, 830))
	bonus_mas_pos.append((953, 807))
	StativeTexture(stative_textures_sprites, (542, 852), (460, 797))
	StativeTexture(stative_textures_sprites, (1396, 849), (1466, 799))
	fighters_mas_pos.append((477, 712))
	fighters_mas_pos.append((1404, 714))
	bonus_mas_pos.append((953, 732))
	StativeTexture(stative_textures_sprites, (464, 855), (349, 734))
	StativeTexture(stative_textures_sprites, (356, 856), (213, 669))
	StativeTexture(stative_textures_sprites, (220, 858), (109, 606))
	StativeTexture(stative_textures_sprites, (132, 871), (0, 533))
	StativeTexture(stative_textures_sprites, (1457, 845), (1562, 734))
	StativeTexture(stative_textures_sprites, (1531, 853), (1681, 676))
	StativeTexture(stative_textures_sprites, (1648, 845), (1793, 623))
	StativeTexture(stative_textures_sprites, (1703, 857), (1918, 545))
	StativeTexture(stative_textures_sprites, (1576, 533), (282, 555))
	return bonus_mas_pos, narkomany, fighters_mas_pos
