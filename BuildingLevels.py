import pygame
import os


stative_textures_sprites = pygame.sprite.Group()
background_sprites = pygame.sprite.Group()
fighter1_sprite = pygame.sprite.Group()
fighter2_sprite = pygame.sprite.Group()


def load_sprite(name, path):
    fullname = os.path.join(path, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print('Cannot load image: ', name)
        raise SystemExit
    image = image.convert_alpha()
    return image


def load_image(folder, name, colorkey=None):
    fullname = os.path.join('data', folder + '/' + name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print('Cannot load image: ', name)
        raise SystemExit
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


class StativeTexture(pygame.sprite.Sprite):
    def __init__(self, group, pos1, pos2):
        super().__init__(group)
        width_sprite = abs(pos2[0] - pos1[0])
        height_sprite = abs(pos2[1] - pos1[1])
        self.image = pygame.Surface((width_sprite, height_sprite))
        self.rect = self.image.get_rect()
        self.rect.x = min(pos1[0], pos2[0])
        self.rect.y = min(pos1[1], pos2[1])


class Background(pygame.sprite.Sprite):
    def __init__(self, group, image):
        super().__init__(group)
        self.image_name = image
        self.image = load_sprite(image, 'fones')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
