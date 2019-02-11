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

    moving_textures_sprites.draw(screen)
    moving_textures_sprites.update()

    unused_sprites.update()
    fighter_sprites.update()
    unused_sprites.draw(screen)
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
        'standing': (
            load_image('fighter1', 'standing1.png'),
            load_image('fighter1', 'standing2.png')
        ),
        'running': (
            load_image('fighter1', 'running1.png'),
            load_image('fighter1', 'running2.png'),
            load_image('fighter1', 'running3.png'),
            load_image('fighter1', 'running4.png')
        ),
        'flying': load_image('fighter1', 'flying.png'),
        'attacking': (
            load_image('fighter1', 'attacking1.png'),
            load_image('fighter1', 'attacking2.png')
        )
    }

    def __init__(self, group):
        super().__init__(group)
        self.falling = 0
        self.image = Fighter1.images['standing'][0]
        self.rect = self.image.get_rect()
        self.width, self.height = self.rect[2], self.rect[3]
        self.rect.x, self.rect.y = 100, 100
        self.direction = 'right'
        self.on_ground = False
        self.attacked, self.attack_time = False, 0

    def update(self):
        if not jumping1:
            if not self.on_ground:
                self.image = self.images['flying']
                self.falling += 0.25
                self.rect.y += 6 + self.falling // 1
                if pygame.sprite.spritecollide(self, stative_textures_sprites, False) \
                        or pygame.sprite.spritecollide(self, moving_textures_sprites, False):
                    self.rect.y -= 6 + self.falling // 1
                    self.falling = 0
                    self.on_ground = True
            else:
                self.rect.y += 6
                if pygame.sprite.spritecollide(self, stative_textures_sprites, False) \
                        or pygame.sprite.spritecollide(self, moving_textures_sprites, False):
                    self.rect.y -= 6
                else:
                    self.image = self.images['flying']
                    self.on_ground = False


class Fighter2(pygame.sprite.Sprite):
    images = {
        'standing': (
            load_image('fighter2', 'standing1.png'),
            load_image('fighter2', 'standing2.png')
        ),
        'running': (
            load_image('fighter2', 'running1.png'),
            load_image('fighter2', 'running2.png'),
            load_image('fighter2', 'running3.png'),
            load_image('fighter2', 'running4.png')
        ),
        'flying': load_image('fighter2', 'flying.png'),
        'attacking': (
            load_image('fighter2', 'attacking1.png'),
            load_image('fighter2', 'attacking2.png')
        )
    }

    def __init__(self, group):
        super().__init__(group)
        self.falling = 0
        self.image = Fighter1.images['standing'][0]
        self.rect = self.image.get_rect()
        self.width, self.height = self.rect[2], self.rect[3]
        self.rect.x, self.rect.y = 810, 100
        self.direction = 'left'
        self.on_ground = False
        self.attacked, self.attack_time = False, 0

    def update(self):
        if not jumping2:
            if not self.on_ground:
                self.image = self.images['flying']
                self.falling += 0.25
                self.rect.y += 6 + self.falling // 1
                if pygame.sprite.spritecollide(self, stative_textures_sprites, False) \
                        or pygame.sprite.spritecollide(self, moving_textures_sprites, False):
                    self.rect.y -= 6 + self.falling // 1
                    self.falling = 0
                    self.on_ground = True
            else:
                self.rect.y += 6
                if pygame.sprite.spritecollide(self, stative_textures_sprites, False) \
                        or pygame.sprite.spritecollide(self, moving_textures_sprites, False):
                    self.rect.y -= 6
                else:
                    self.image = self.images['flying']
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

counter, running, clock, fps = 0, True, pygame.time.Clock(), 60

jumping1 = False
jumping2 = False
jumped1 = 20
jumped2 = 20
jj1 = 10
jj2 = 10

while running:
    counter += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()

    if jumping1:
        jumped1 -= 1
        jj1 -= 0.5
        fighter1.rect.y -= jj1 // 1
        if pygame.sprite.spritecollide(fighter1, stative_textures_sprites, False) \
                or pygame.sprite.spritecollide(fighter1, moving_textures_sprites, False):
            fighter1.rect.y += jj1 // 1
            jumped1 = 20
            jj1 = 10
            jumping1 = False
        if jumped1 == 0:
            jumped1 = 20
            jj1 = 10
            jumping1 = False

    if jumping2:
        jumped2 -= 1
        jj2 -= 0.5
        fighter2.rect.y -= jj2 // 1
        if pygame.sprite.spritecollide(fighter2, stative_textures_sprites, False) \
                or pygame.sprite.spritecollide(fighter2, moving_textures_sprites, False):
            fighter2.rect.y += jj2 // 1
            jumped2 = 20
            jj2 = 10
            jumping2 = False
        if jumped1 == 0:
            jumped2 = 20
            jj2 = 10
            jumping2 = False

    if pressed[pygame.K_d]:
        if not jumping1:
            fighter1.direction = 'right'
            if not counter % 10:
                if fighter1.image == fighter1.images['running'][0]:
                    fighter1.image = fighter1.images['running'][1]
                else:
                    fighter1.image = fighter1.images['running'][0]

        fighter1.rect.x += 5
        if pygame.sprite.spritecollide(fighter1, stative_textures_sprites, False) \
                or pygame.sprite.spritecollide(fighter1, moving_textures_sprites, False):
            fighter1.rect.x -= 5

    if pressed[pygame.K_a]:
        if not jumping1:
            fighter1.direction = 'left'
            if not counter % 10:
                if fighter1.image == fighter1.images['running'][2]:
                    fighter1.image = fighter1.images['running'][3]
                else:
                    fighter1.image = fighter1.images['running'][2]

        fighter1.rect.x -= 5
        if pygame.sprite.spritecollide(fighter1, stative_textures_sprites, False) \
                or pygame.sprite.spritecollide(fighter1, moving_textures_sprites, False):
            fighter1.rect.x += 5

    if not pressed[pygame.K_d] and not pressed[pygame.K_a] and not jumping1 and fighter2.on_ground:
        if fighter1.direction == 'left':
            fighter1.image = fighter1.images['standing'][1]
        else:
            fighter1.image = fighter1.images['standing'][0]

    if pressed[pygame.K_w]:
        if fighter1.on_ground:
            fighter1.image = fighter1.images['flying']
            fighter1.on_ground = False
            jumping1 = True

    if pressed[pygame.K_s]:
        if fighter1.attack_time >= 250:
            fighter1.attacked = False
            fighter1.attack_time = 0
        if not fighter1.attacked:
            fighter1.attack_time += 1
            if fighter1.attack_time <= 5:
                if fighter1.direction == 'left':
                    fighter1.image = fighter1.images['attacking'][1]
                else:
                    fighter1.image = fighter1.images['attacking'][0]
            else:
                fighter1.attacked = True

    if fighter1.attacked:
        fighter1.attack_time += 1

    if pressed[pygame.K_RIGHT]:
        if not jumping2:
            fighter2.direction = 'right'
            if not counter % 10:
                if fighter2.image == fighter2.images['running'][2]:
                    fighter2.image = fighter2.images['running'][3]
                else:
                    fighter2.image = fighter2.images['running'][2]

        fighter2.rect.x += 5
        if pygame.sprite.spritecollide(fighter2, stative_textures_sprites, False) \
                or pygame.sprite.spritecollide(fighter2, moving_textures_sprites, False):
            fighter2.rect.x -= 5

    if pressed[pygame.K_LEFT]:
        if not jumping2:
            fighter2.direction = 'left'
            if not counter % 10:
                if fighter2.image == fighter2.images['running'][0]:
                    fighter2.image = fighter2.images['running'][1]
                else:
                    fighter2.image = fighter2.images['running'][0]

        fighter2.rect.x -= 5
        if pygame.sprite.spritecollide(fighter2, stative_textures_sprites, False) \
                or pygame.sprite.spritecollide(fighter2, moving_textures_sprites, False):
            fighter2.rect.x += 5

    if not pressed[pygame.K_RIGHT] and not pressed[pygame.K_LEFT] and not jumping2 and fighter2.on_ground:
        if fighter2.direction == 'left':
            fighter2.image = fighter2.images['standing'][0]
        else:
            fighter2.image = fighter2.images['standing'][1]

    if pressed[pygame.K_UP]:
        if fighter2.on_ground:
            fighter2.image = fighter2.images['flying']
            fighter2.on_ground = False
            jumping2 = True

    if pressed[pygame.K_DOWN]:
        if fighter2.attack_time >= 250:
            fighter2.attacked = False
            fighter2.attack_time = 0
        if not fighter2.attacked:
            fighter2.attack_time += 1
            if fighter2.attack_time <= 5:
                if fighter2.direction == 'left':
                    fighter2.image = fighter2.images['attacking'][0]
                else:
                    fighter2.image = fighter2.images['attacking'][1]
            else:
                fighter2.attacked = True

    if fighter2.attacked:
        fighter2.attack_time += 1

    screen_update()

pygame.quit()
