import pygame
import os

size = screen_width, screen_height = 960, 540
screen = pygame.display.set_mode(size)
# I'm happy


def load_texture(name):
    fullname = os.path.join('sprites', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print('Cannot load image: ', name)
        raise SystemExit
    image = image.convert_alpha()
    return image


def screen_update():
    screen.fill(pygame.Color('#ffffff'))

    stative_textures_sprites.draw(screen)
    stative_textures_sprites.update()

    moving_textures_sprites.draw(screen)
    moving_textures_sprites.update()

    unused_sprites.update()
    fighter_sprites.update()
    fighter_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(fps)


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


class Fighter1(pygame.sprite.Sprite):
    images = {
        'standing': load_image('fighter1', 'standing.png')
    }

    def __init__(self, group):
        super().__init__(group)
        self.image = Fighter1.images['standing']
        self.rect = self.image.get_rect()
        self.width, self.height = self.rect[2], self.rect[3]
        self.rect.x, self.rect.y = 100, 100

    def update(self):
        if not clone1.on_ground:
            self.rect.y += 3


class Fighter2(pygame.sprite.Sprite):
    images = {
        'standing': load_image('fighter2', 'standing.png')
    }

    def __init__(self, group):
        super().__init__(group)
        self.image = Fighter1.images['standing']
        self.rect = self.image.get_rect()
        self.width, self.height = self.rect[2], self.rect[3]
        self.rect.x, self.rect.y = 810, 100
        self.on_ground = False

    def update(self):
        if not clone2.on_ground:
            self.rect.y += 3


class Clone1(pygame.sprite.Sprite):
    images = {
        'standing': load_image('fighter1', 'standing.png')
    }

    def __init__(self, group):
        super().__init__(group)
        self.image = Fighter1.images['standing']
        self.rect = self.image.get_rect()
        self.width, self.height = self.rect[2], self.rect[3]
        self.rect.x, self.rect.y = 100, 100
        self.on_ground = False

    def update(self):
        if not self.on_ground:
            self.rect.y += 3
            if pygame.sprite.spritecollide(self, stative_textures_sprites, False) \
                    or pygame.sprite.spritecollide(self, moving_textures_sprites, False):
                self.rect.y -= 3
                self.on_ground = True
        else:
            self.rect.y += 3
            if pygame.sprite.spritecollide(self, stative_textures_sprites, False) \
                    or pygame.sprite.spritecollide(self, moving_textures_sprites, False):
                self.rect.y -= 3
            else:
                self.on_ground = False


class Clone2(pygame.sprite.Sprite):
    images = {
        'standing': load_image('fighter2', 'standing.png')
    }

    def __init__(self, group):
        super().__init__(group)
        self.image = Fighter1.images['standing']
        self.rect = self.image.get_rect()
        self.width, self.height = self.rect[2], self.rect[3]
        self.rect.x, self.rect.y = 810, 100
        self.on_ground = False

    def update(self):
        if not self.on_ground:
            self.rect.y += 3
            if pygame.sprite.spritecollide(self, stative_textures_sprites, False) \
                    or pygame.sprite.spritecollide(self, moving_textures_sprites, False):
                self.rect.y -= 3
                self.on_ground = True
        else:
            self.rect.y += 3
            if pygame.sprite.spritecollide(self, stative_textures_sprites, False) \
                    or pygame.sprite.spritecollide(self, moving_textures_sprites, False):
                self.rect.y -= 3
            else:
                self.on_ground = False


class MovingTexture(pygame.sprite.Sprite):
    def __init__(self, group, x, y, object_name):
        super().__init__(group)
        self.image = load_texture(object_name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class StativeTexture(pygame.sprite.Sprite):
    def __init__(self, group, x1, y1, x2, y2):
        super().__init__(group)
        width_sprite = x2 - x1
        height_sprite = y2 - y1
        self.image = pygame.Surface((width_sprite, height_sprite))
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1


stative_textures_sprites = pygame.sprite.Group()
moving_textures_sprites = pygame.sprite.Group()
unused_sprites = pygame.sprite.Group()

clone1 = Clone1(unused_sprites)
clone2 = Clone2(unused_sprites)

box1 = MovingTexture(stative_textures_sprites, 150, 425, 'medium_box.png')
box2 = MovingTexture(stative_textures_sprites, 350, 400, 'big_box.png')
box3 = MovingTexture(stative_textures_sprites, 600, 450, 'small_box.png')
box4 = MovingTexture(stative_textures_sprites, 750, 425, 'medium_box.png')

sad = StativeTexture(stative_textures_sprites, 0, 500, 960, 540)
asd = StativeTexture(stative_textures_sprites, 0, 0, 960, 40)
sdf = StativeTexture(stative_textures_sprites, 0, 0, 40, 540)
dfg = StativeTexture(stative_textures_sprites, 920, 0, 960, 540)
dyt = StativeTexture(stative_textures_sprites, 100, 250, 860, 290)

fighter_sprites = pygame.sprite.Group()
fighter1 = Fighter1(fighter_sprites)
fighter2 = Fighter2(fighter_sprites)

counter, running, clock, ticks = 0, True, pygame.time.Clock(), 200


fps = 150

while running:
    counter += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_d]:
        clone1.rect.x += 2
        if pygame.sprite.spritecollide(clone1, stative_textures_sprites, False) \
                or pygame.sprite.spritecollide(clone1, moving_textures_sprites, False):
            clone1.rect.x -= 2
        else:
            fighter1.rect.x += 2

    if pressed[pygame.K_a]:
        clone1.rect.x -= 2
        if pygame.sprite.spritecollide(clone1, stative_textures_sprites, False) \
                or pygame.sprite.spritecollide(clone1, moving_textures_sprites, False):
            clone1.rect.x += 2
        else:
            fighter1.rect.x -= 2

    if pressed[pygame.K_SPACE]:
        clone1.rect.y -= 4
        if pygame.sprite.spritecollide(clone1, stative_textures_sprites, False) \
                or pygame.sprite.spritecollide(clone1, moving_textures_sprites, False):
            clone1.rect.y += 4
        else:
            fighter1.rect.y -= 4

    if pressed[pygame.K_RIGHT]:
        clone2.rect.x += 2
        if pygame.sprite.spritecollide(clone2, stative_textures_sprites, False) \
                or pygame.sprite.spritecollide(clone2, moving_textures_sprites, False):
            clone2.rect.x -= 2
        else:
            fighter2.rect.x += 2

    if pressed[pygame.K_LEFT]:
        clone2.rect.x -= 2
        if pygame.sprite.spritecollide(clone2, stative_textures_sprites, False) \
                or pygame.sprite.spritecollide(clone2, moving_textures_sprites, False):
            clone2.rect.x += 2
        else:
            fighter2.rect.x -= 2

    if pressed[pygame.K_l]:
        clone2.rect.y -= 4
        if pygame.sprite.spritecollide(clone2, stative_textures_sprites, False) \
                or pygame.sprite.spritecollide(clone2, moving_textures_sprites, False):
            clone2.rect.y += 4
        else:
            fighter2.rect.y -= 4

    screen_update()

pygame.quit()  # Выход
