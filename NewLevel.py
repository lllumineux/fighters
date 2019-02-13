from BuildingLevels import load_sprite, Background, StativeTexture, stative_textures_sprites,          background_sprites, fighter1_sprite, fighter2_sprite

def building():
	narkomany = False
	background = Background(background_sprites, 'lave.jpg')
	StativeTexture(stative_textures_sprites, (488, 348), (771, 486))
	StativeTexture(stative_textures_sprites, (72, 759), (1771, 686))
