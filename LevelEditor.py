import pygame
import os

size = screen_width, screen_height = 1920, 1080
screen = pygame.display.set_mode(size)


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


def draw_object(pos1, pos2):
    mas_act.append(StativeTexture(objects_sprites, pos1, pos2))


def draw_stickman(spos):
    mas_act.append(Fighter(objects_sprites, spos))


class Fighter(pygame.sprite.Sprite):

    def __init__(self, group, spos):
        super().__init__(group)
        self.falling = 0
        self.image = load_image('fighter1', 'standing1.png')
        self.rect = self.image.get_rect()
        self.width, self.height = self.rect[2], self.rect[3]
        self.rect.x, self.rect.y = spos
        self.direction = 'right'
        self.on_ground = False
        self.attacked, self.attack_time = False, 0
        self.hp = 3


class StativeTexture(pygame.sprite.Sprite):
    def __init__(self, group, pos1, pos2):
        super().__init__(group)
        width_sprite = abs(pos2[0] - pos1[0])
        height_sprite = abs(pos2[1] - pos1[1])
        self.image = pygame.Surface((width_sprite, height_sprite))
        self.rect = self.image.get_rect()
        self.rect.x = min(pos1[0], pos2[0])
        self.rect.y = min(pos1[1], pos2[1])


class FoneMini(pygame.sprite.Sprite):
    def __init__(self, group, x, y, image):
        super().__init__(group)
        self.image_name = image
        self.image = load_sprite(image, 'fones_miniaturs')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_event(self, spos):
        if self.rect.collidepoint(spos):
            global fone_name
            fone_name = self.image_name


class Background(pygame.sprite.Sprite):
    def __init__(self, group, image):
        super().__init__(group)
        self.image_name = image
        self.image = load_sprite(image, 'fones')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


def screen_update_choose_fone():
    screen.fill((0, 0, 0))
    mini_fone_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(fps)


def screen_update():
    screen.fill((0, 0, 0))
    background_sprites.draw(screen)
    objects_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(fps)


mini_fone_sprites = pygame.sprite.Group()
background_sprites = pygame.sprite.Group()
objects_sprites = pygame.sprite.Group()

flash = FoneMini(mini_fone_sprites, 0, 0, 'flash.jpg')

lave = FoneMini(mini_fone_sprites, 640, 0, 'lave.jpg')

perfecto = FoneMini(mini_fone_sprites, 1280, 0, 'perfecto.jpg')

redline = FoneMini(mini_fone_sprites, 0, 360, 'redline.jpg')

redone = FoneMini(mini_fone_sprites, 640, 360, 'redone.jpg')

storm = FoneMini(mini_fone_sprites, 1280, 360, 'storm.jpg')

white = FoneMini(mini_fone_sprites, 0, 720, 'white.png')

narko = FoneMini(mini_fone_sprites, 1280, 720, 'narko.png')

running, clock, fps = True, pygame.time.Clock(), 60
fone_name = None

exit_code = False
narkomany = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_code = True
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # При нажатии мыши
            pos = pygame.mouse.get_pos()
            for i in mini_fone_sprites:
                i.get_event(pos)
                if fone_name:
                    break
    if fone_name:
        if fone_name == 'narko.png':
            narkomany = True
        else:
            narkomany = False
            fone = Background(background_sprites, fone_name)
        running = False

    screen_update_choose_fone()

if not exit_code:
    positioning = False
    running = True
    spos1 = None
    spos2 = None
    mas_act = []
    mas_write = []
    fighter1 = None
    fighter2 = None

    with open('NewLevel.py', 'w') as f:
        f.write('from BuildingLevels import load_sprite, Background, StativeTexture, stative_textures_sprites, \
         background_sprites, fighter1_sprite, fighter2_sprite' '\n' + '\n')
        f.write('def building():' + '\n')
        if narkomany:
            f.write('\t' + 'narkomany = True' + '\n')
        else:
            f.write('\t' + 'narkomany = False' + '\n')
            f.write('\t' + 'background = Background(background_sprites, ' + "'" + fone_name + "'" + ')' + '\n')

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stroka = ''
                    for i in mas_write:
                        stroka += i
                    f.write(stroka)
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if event.button == 1:
                        spos2 = pygame.mouse.get_pos()
                        if not positioning:
                            positioning = True
                            spos1 = spos2

                        else:
                            draw_object(spos1, spos2)
                            stroka = '\t' + 'StativeTexture(stative_textures_sprites, '\
                                     + str(spos1) + ', ' + str(spos2) + ')' + '\n'
                            mas_write.append(stroka)
                            positioning = False

                    elif event.button == 2 and not fighter2:  # Not ready
                        pos = pygame.mouse.get_pos()

                        draw_stickman(pos)

                        if not fighter1:
                            stroka = '\t' + 'Fighter(fighter1_sprite, ' + str(pos) + ')' + '\n'
                        else:
                            stroka = '\t' + 'Fighter(fighter2_sprite, ' + str(pos) + ')' + '\n'

                        mas_write.append(stroka)
                    elif event.button == 3:
                        pass
                        # Сделай бонусы

                if event.type == 2:
                    if positioning:
                        positioning = False
                    else:
                        try:
                            objects_sprites.remove(mas_act[-1])
                            mas_act.pop(-1)
                            mas_write.pop(-1)
                        except IndexError:
                            pass

            screen_update()

pygame.quit()
