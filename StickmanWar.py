import pygame
import os

size = screen_width, screen_height = 960, 540
screen = pygame.display.set_mode(size)


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

    for obj in fighter_sprites:
        obj.update()
    fighter_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(fps)


def load_image(folder, name, colorkey=None):
    fullname = os.path.join('data', folder + '/' + name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
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

        self.width, self.height = 50, 105
        self.x, self.y = 0, screen_height - self.height
        self.on_ground = False

    def update(self):
        if self.y < screen_height - self.height:
            self.on_ground = False
        else:
            self.on_ground = True

        if not self.on_ground:
            self.y += 500 * dt

        self.rect.topleft = self.x, self.y


class Fighter2(pygame.sprite.Sprite):
    images = {
        'standing': load_image('fighter2', 'standing.png')
    }

    def __init__(self, group):
        super().__init__(group)
        self.image = Fighter1.images['standing']
        self.rect = self.image.get_rect()

        self.width, self.height = 50, 105
        self.x, self.y = screen_width - self.width, screen_height - self.height
        self.on_ground = False

    def update(self):
        if self.y < screen_height - self.height:
            self.on_ground = False
        else:
            self.on_ground = True

        if not self.on_ground:
            self.y += 500 * dt

        self.rect.topleft = self.x, self.y


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


fps = 50

while running:
    counter += 1
    dt = clock.get_time() / 500

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_d]:
        fighter1.x += 200 * dt

    if pressed[pygame.K_a]:
        fighter1.x -= 200 * dt

    if pressed[pygame.K_SPACE]:
        fighter1.y -= 1000 * dt

    if pressed[pygame.K_RIGHT]:
        fighter2.x += 200 * dt

    if pressed[pygame.K_LEFT]:
        fighter2.x -= 200 * dt

    if pressed[pygame.K_l]:
        fighter2.y -= 1000 * dt

    screen_update()

pygame.quit()  # Выход
