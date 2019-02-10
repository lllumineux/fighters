import os
import pygame


screen_size = screen_width, screen_height = 960, 540
screen = pygame.display.set_mode(screen_size)
screen.fill(pygame.Color('#ffffff'))


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


fighter_sprites = pygame.sprite.Group()
fighter1 = Fighter1(fighter_sprites)
fighter2 = Fighter2(fighter_sprites)

counter, running, clock, ticks = 0, True, pygame.time.Clock(), 200


def screen_update():
    screen.fill(pygame.Color('#ffffff'))

    for obj in fighter_sprites:
        obj.update()
    fighter_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(ticks)


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
pygame.quit()
