import pygame.font
from pygame.sprite import Group
from test_ship import Ship
from PyQt5.QtGui import QColor

# class Scoreboard:
#     def __init__(self, s_game):
#         self.game = s_game
#         self.screen = s_game.screen
#         self.screen_rect = self.screen.get_rect()
#         self.setting = s_game.setting
#         self.stats = s_game.stats
#         self.text_color = (30, 30, 30)
#         self.font = pygame.font.SysFont(None, 66)
#         self.level = pygame.font.SysFont(None, 66)
#         self.prep_score()
#         self.prep_high_score()
#         self.prep_ships()
#         self.prep_level()

#     def prep_ships(self):
#         self.ships = Group()
#         for ship_number in range(self.stats.ships_left):
#             ship = Ship(self.game)
#             ship.rect.x = 10 + ship_number * ship.rect.width
#             ship.rect.y = 10
#             #self.ships.add(ship)

#     def prep_score(self):
#         self.score_str = str(self.stats.score/4)
#         # rounded_score = round(self.stats.score, -1)
#         # score_str = '{:,}'.format(score_str)
#         self.score_image = self.font.render(self.score_str, True, self.text_color)
#         self.score_rect = self.score_image.get_rect()
#         self.score_rect.right = self.screen_rect.right - 10
#         self.score_rect.top = 14

#     def prep_level(self):
#         self.level_image = self.font.render(str(self.stats.level), True,
#                                             self.text_color)
#         self.level_image_rect = self.level_image.get_rect()
#         self.level_rect = self.level_image_rect

#         self.level_image_rect.top = 5
#         self.level_image_rect.left = 179

#     def prep_high_score(self):
#         high_score = self.stats.high_score
#         high_score_str = '{:,}'.format(high_score)
#         self.high_score_image = self.font.render(high_score_str, True,
#                                                  self.text_color)
#         # Center the high score at the top of screen
#         self.high_score_rect = self.high_score_image.get_rect()
#         self.high_score_rect.centerx = self.screen_rect.centerx
#         self.high_score_rect.top = self.score_rect.top

#     def blit_score_gold(self):
#         self.score_image2 = self.font.render(str(self.stats.score), True, (250, 250, 250))
#         self.gold_image2 = self.font.render(str(self.score_str), True, (250, 250, 250))
#         self.screen.blit(self.score_image2, (1100, 733))
#         self.screen.blit(self.gold_image2, (1100, 803))

#     def show_score(self):
#         self.screen.blit(self.score_image, self.score_rect)

#         self.screen.blit(self.high_score_image, self.high_score_rect)
#         self.screen.blit(self.level_image, self.level_rect)


#     def check_high_score(self):
#         if self.stats.score > self.stats.high_score:
#             self.stats.high_score = self.stats.score
#             self.prep_high_score()
import pygame.font

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, game):
        """Initialize scorekeeping attributes."""
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = game.stats
        self.setting = game.setting

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Load the highest score
        self.high_score = self.load_high_score()

        self.prep_score()
        self.prep_high_score()

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10


    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True,
                                            self.text_color)
        self.level_image_rect = self.level_image.get_rect()
        self.level_rect = self.level_image_rect

        self.level_image_rect.top = 5
        self.level_image_rect.left = 179
        

    def prep_score(self):
        """Turn the score into a rendered image."""
        self.score_str = str(self.stats.score)
        
        self.score_image = self.font.render(self.score_str, True, self.text_color)
        
        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the highest score into a rendered image."""
        high_score_str = f"High Score: {self.high_score}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        # Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def show_score(self):
        """Draw scores to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def check_high_score(self):
        """Check if there's a new high score and save it."""
        if self.stats.score > self.high_score:
            self.high_score = self.stats.score
            self.save_high_score()
            self.prep_high_score()  # Update the display

    def save_high_score(self):
        """Save the highest score to a file."""
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def load_high_score(self):
        """Load the highest score from a file."""
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read().strip())
        except (FileNotFoundError, ValueError):
            return 0  # Default high score if the file doesn't exist

    def blit_score_gold(self):
        self.score_image2 = self.font.render(str(self.stats.score), True, (250, 250, 250))
        self.gold_image2 = self.font.render(str(self.score_str), True, (250, 250, 250))
        self.screen.blit(self.score_image2, (1100, 733))
        self.screen.blit(self.gold_image2, (1100, 803))
