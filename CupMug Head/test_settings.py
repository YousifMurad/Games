import pygame


class Settings:
    def __init__(self):
        self.ship_speed=self.bullet_speed=self.alien_speed=self.fleet_direction=self.alien_points=self.level=self.ship_limit=None
        self.screen_width = 1920
        self.screen_height = 1080
        n = "Forest1.jpg"
        self.background = pygame.image.load("gameConcept/Forest1.jpg")
        self.bg_color = (240, 244, 33)
        self.level_text = pygame.image.load("gameConcept\level45.png")
        self.souls = pygame.image.load("gameConcept/Souls.png")
        self.souls_rect = self.souls.get_rect()
        self.coin = pygame.image.load("gameConcept\coin55.png")
        self.game_over = pygame.image.load("gameConcept\game_result.png")
        self.losing_image = pygame.image.load("gameConcept/removal_these.png")
        self.losing_phrase = pygame.image.load("gameConcept/bd9cf6e5-a818-4d51-8a81-8e279cf5e86e.png")
        self.losing_sound = pygame.mixer.Sound("gameConcept\game-over-sound-effects-eddited.mp3")
        self.bullet_shot = pygame.mixer.Sound("gameConcept\cuphead-weapons-sound2.mp3")
       
        self.bullet_allowed = 15
        # how quickly the game's speed increased :
        self.speedUp_scale = 1.1
        # how quickly alien point will increase :
        self.score_scale = 1.5

        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        self.ship_limit = 2
        self.ship_speed = 5.5
        self.bullet_speed = 8.0
        self.alien_speed = 2
        self.fleet_direction = 1
        self.alien_points = 1
        self.level = 1

    def increase_speed(self):
        self.ship_speed *= self.speedUp_scale
        self.bullet_speed *= self.speedUp_scale
        self.alien_speed *= self.speedUp_scale
        self.alien_points = int(self.alien_points * self.score_scale)
