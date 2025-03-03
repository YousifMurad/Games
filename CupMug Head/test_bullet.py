import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, sj_game, bullet_position='midright'):
        super().__init__()
        self.screen = sj_game.screen
        self.settings = sj_game.setting
        # self.color = self.settings.bullet_color
        self.bulletImg = pygame.image.load("F:\CupMug Head\gameConcept/1st_bullet--1-.png")
        self.rect = self.bulletImg.get_rect()
        if bullet_position == 'midright':
            self.rect.midright = sj_game.ship.rect.midright
        else:
            self.rect.midright = sj_game.ship.rect.topright
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def create_bullet(self):
        self.screen.blit(self.bulletImg, self.rect)
