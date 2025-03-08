import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, sj_game):
        super().__init__()
        self.screen = sj_game.screen
        self.settings = sj_game.setting
        self.image = pygame.image.load('F:\CupMug Head\gameConcept\king_dice (1).png')
        self.rect = self.image.get_rect()
        self.rect.x = 1250
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)
        self.initialize_dynamic_setting()

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.left <= 0:
            return True

    def initialize_dynamic_setting(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1
        self.fleet_direction = 1
        self.alien_points = 1

    def update(self):
        #"""Move the alien to the right"""
        self.x -= self.settings.alien_speed*(self.settings.fleet_direction)
        self.rect.x = self.x


