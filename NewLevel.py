from BuildingLevels import load_sprite, Background, StativeTexture, stative_textures_sprites,          background_sprites, fighter1_sprite, fighter2_sprite

def building():
	narkomany = False
	background = Background(background_sprites, 'flash.jpg')
	Fighter(fighter1_sprite, (551, 194))
	Fighter(fighter1_sprite, (1123, 263))
	Fighter(fighter1_sprite, (776, 327))
	Fighter(fighter1_sprite, (485, 431))
	StativeTexture(stative_textures_sprites, (312, 563), (1496, 609))
