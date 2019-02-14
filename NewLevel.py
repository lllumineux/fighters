from BuildingLevels import Background, StativeTexture, stative_textures_sprites,\
	background_sprites


def building():
	global bonus_mas_pos
	global narkomany
	global background
	bonus_mas_pos = []
	fighters_mas_pos = []
	narkomany = False
	background = Background(background_sprites, 'lave.jpg')
	StativeTexture(stative_textures_sprites, (398, 663), (1383, 752))
	StativeTexture(stative_textures_sprites, (862, 275), (971, 693))
	fighters_mas_pos.append((1178, 528))
	fighters_mas_pos.append((598, 512))
	bonus_mas_pos.append((773, 566))
	bonus_mas_pos.append((1017, 593))
	bonus_mas_pos.append((500, 592))
	bonus_mas_pos.append((1180, 620))
	return bonus_mas_pos, narkomany, fighters_mas_pos
