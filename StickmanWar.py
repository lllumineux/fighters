import pygame
import os
from BuildingLevels import load_sprite, Background, StativeTexture, stative_textures_sprites, background_sprites, \
    fighter1_sprite, fighter2_sprite
from NewLevel import building

size = screen_width, screen_height = 1920, 1080
screen = pygame.display.set_mode(size)


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


def screen_update():
    screen.fill(pygame.Color('#ffffff'))

    stative_textures_sprites.draw(screen)
    stative_textures_sprites.update()

    fighter1_sprite.update()
    fighter2_sprite.update()
    fighter1_sprite.draw(screen)
    fighter2_sprite.draw(screen)

    ball1_sprite.update()
    ball1_sprite.draw(screen)
    ball2_sprite.update()
    ball2_sprite.draw(screen)

    pygame.display.flip()
    clock.tick(fps)


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
        'jumping': (
            load_image('fighter1', 'jumping1.png'),
            load_image('fighter1', 'jumping2.png'),
        ),
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
        self.hp = 3

    def update(self):
        if not jumping1:
            if not self.on_ground:
                if fighter1.direction == 'left':
                    fighter1.image = fighter1.images['jumping'][0]
                else:
                    fighter1.image = fighter1.images['jumping'][1]
                self.falling += 0.25
                self.rect.y += 6 + self.falling // 1
                if pygame.sprite.spritecollide(self, stative_textures_sprites, False):
                    self.rect.y -= 6 + self.falling // 1
                    self.falling = 0
                    self.on_ground = True
            else:
                self.rect.y += 6
                if pygame.sprite.spritecollide(self, stative_textures_sprites, False):
                    self.rect.y -= 6
                else:
                    if fighter1.direction == 'left':
                        fighter1.image = fighter1.images['jumping'][0]
                    else:
                        fighter1.image = fighter1.images['jumping'][1]
                    self.on_ground = False

        if not self.on_ground:
            if fighter1.direction == 'left':
                fighter1.image = fighter1.images['jumping'][0]
            else:
                fighter1.image = fighter1.images['jumping'][1]


class Ball1(pygame.sprite.Sprite):
    image = load_image('fighter1', 'ball.png')

    def __init__(self, group):
        super().__init__(group)
        self.falling = 0
        self.image = Ball1.image
        self.rect = self.image.get_rect()
        self.width, self.height = 14, 14
        self.rect.x, self.rect.y = fighter1.rect.x + 31, fighter1.rect.y + 26
        self.direction = fighter1.direction

    def update(self):
        if self.direction == 'left':
            self.rect.x -= 10
        elif self.direction == 'right':
            self.rect.x += 10

        if pygame.sprite.spritecollide(ball1, fighter2_sprite, False):
            fighter2.hp -= 1
            ball1.rect.x, ball1.rect.y = 9999, 9999
            ball1.direction = 'none'
        if fighter2.hp == 0:
            print('First player won!')

        if (
            pygame.sprite.spritecollide(ball1, stative_textures_sprites, False) or
            pygame.sprite.spritecollide(ball1, ball2_sprite, False)
        ):
            ball1.rect.x, ball1.rect.y = 9999, 9999
            ball1.direction = 'none'


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
        'jumping': (
            load_image('fighter2', 'jumping1.png'),
            load_image('fighter2', 'jumping2.png'),
        ),
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
        self.hp = 3

    def update(self):
        if not jumping2:
            if not self.on_ground:
                self.falling += 0.25
                self.rect.y += 6 + self.falling // 1
                if pygame.sprite.spritecollide(self, stative_textures_sprites, False):
                    self.rect.y -= 6 + self.falling // 1
                    self.falling = 0
                    self.on_ground = True
            else:
                self.rect.y += 6
                if pygame.sprite.spritecollide(self, stative_textures_sprites, False):
                    self.rect.y -= 6
                else:
                    self.on_ground = False

        if not self.on_ground:
            if fighter2.direction == 'left':
                fighter2.image = fighter2.images['jumping'][0]
            else:
                fighter2.image = fighter2.images['jumping'][1]


class Ball2(pygame.sprite.Sprite):
    image = load_image('fighter2', 'ball.png')

    def __init__(self, group):
        super().__init__(group)
        self.falling = 0
        self.image = Ball2.image
        self.rect = self.image.get_rect()
        self.width, self.height = 14, 14
        self.rect.x, self.rect.y = fighter2.rect.x + 31, fighter2.rect.y + 26
        self.direction = fighter2.direction

    def update(self):
        if self.direction == 'left':
            self.rect.x -= 10
        elif self.direction == 'right':
            self.rect.x += 10

        if pygame.sprite.spritecollide(ball2, fighter1_sprite, False):
            fighter1.hp -= 1
            ball2.rect.x, ball2.rect.y = 9999, 9999
            ball2.direction = 'none'
        if fighter1.hp == 0:
            print('Second player won!')

        if (
            pygame.sprite.spritecollide(ball2, stative_textures_sprites, False) or
            pygame.sprite.spritecollide(ball2, ball1_sprite, False)
        ):
            ball2.rect.x, ball2.rect.y = 9999, 9999
            ball2.direction = 'none'


fighter1 = Fighter1(fighter1_sprite)
fighter2 = Fighter2(fighter2_sprite)

ball1_sprite = pygame.sprite.Group()
ball2_sprite = pygame.sprite.Group()
building()

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
            print(counter)
            running = False

    pressed = pygame.key.get_pressed()

    if jumping1:
        jumped1 -= 1
        jj1 -= 0.5
        fighter1.rect.y -= jj1 // 1
        if pygame.sprite.spritecollide(fighter1, stative_textures_sprites, False):
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
        if pygame.sprite.spritecollide(fighter2, stative_textures_sprites, False):
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
            if not counter % 7:
                if fighter1.image == fighter1.images['running'][0]:
                    fighter1.image = fighter1.images['running'][1]
                else:
                    fighter1.image = fighter1.images['running'][0]

        fighter1.rect.x += 5
        if pygame.sprite.spritecollide(fighter1, stative_textures_sprites, False):
            fighter1.rect.x -= 5

    if pressed[pygame.K_a]:
        if not jumping1:
            fighter1.direction = 'left'
            if not counter % 7:
                if fighter1.image == fighter1.images['running'][2]:
                    fighter1.image = fighter1.images['running'][3]
                else:
                    fighter1.image = fighter1.images['running'][2]

        fighter1.rect.x -= 5
        if pygame.sprite.spritecollide(fighter1, stative_textures_sprites, False):
            fighter1.rect.x += 5

    if not pressed[pygame.K_d] and not pressed[pygame.K_a] and not jumping1 and fighter2.on_ground:
        if fighter1.direction == 'left':
            fighter1.image = fighter1.images['standing'][1]
        else:
            fighter1.image = fighter1.images['standing'][0]

    if pressed[pygame.K_w]:
        if fighter1.on_ground:
            fighter1.on_ground = False
            jumping1 = True

    if pressed[pygame.K_s]:
        if fighter1.attack_time >= 100:
            fighter1.attacked = False
            fighter1.attack_time = 0
        if not fighter1.attacked:
            fighter1.attack_time += 1
            if fighter1.attack_time == 1:
                ball1 = Ball1(ball1_sprite)
            elif fighter1.attack_time <= 5:
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
            if not counter % 7:
                if fighter2.image == fighter2.images['running'][2]:
                    fighter2.image = fighter2.images['running'][3]
                else:
                    fighter2.image = fighter2.images['running'][2]

        fighter2.rect.x += 5
        if pygame.sprite.spritecollide(fighter2, stative_textures_sprites, False):
            fighter2.rect.x -= 5

    if pressed[pygame.K_LEFT]:
        if not jumping2:
            fighter2.direction = 'left'
            if not counter % 7:
                if fighter2.image == fighter2.images['running'][0]:
                    fighter2.image = fighter2.images['running'][1]
                else:
                    fighter2.image = fighter2.images['running'][0]

        fighter2.rect.x -= 5
        if pygame.sprite.spritecollide(fighter2, stative_textures_sprites, False):
            fighter2.rect.x += 5

    if not pressed[pygame.K_RIGHT] and not pressed[pygame.K_LEFT] and not jumping2 and fighter2.on_ground:
        if fighter2.direction == 'left':
            fighter2.image = fighter2.images['standing'][0]
        else:
            fighter2.image = fighter2.images['standing'][1]

    if pressed[pygame.K_UP]:
        if fighter2.on_ground:
            fighter2.on_ground = False
            jumping2 = True

    if pressed[pygame.K_DOWN]:
        if fighter2.attack_time >= 100:
            fighter2.attacked = False
            fighter2.attack_time = 0
        if not fighter2.attacked:
            fighter2.attack_time += 1
            if fighter2.attack_time == 1:
                ball2 = Ball2(ball2_sprite)
            elif fighter2.attack_time <= 5:
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
