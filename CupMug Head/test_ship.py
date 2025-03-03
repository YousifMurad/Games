import pygame
from pygame import sprite


class Ship:
    def __init__(self, sj_game, ch_name='cup_head'):
        super().__init__()
        self.screen = sj_game.screen
        self.screen_rect = sj_game.screen.get_rect()
        self.image = pygame.image.load(f'F:\CupMug Head\gameConcept\{ch_name}.png')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.settings = sj_game.setting
        self.y = float(self.rect.y)
        self.moving_down = False
        self.moving_up = False

    def blitme(self):

        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_down:
            if self.rect.bottom < 1080:
                self.y += self.settings.ship_speed

        if self.moving_up:
            if self.rect.top > 100:
                self.y -= self.settings.ship_speed
        self.rect.y = self.y

    def center_ship(self):
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)







