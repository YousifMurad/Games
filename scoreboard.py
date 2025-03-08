import pygame.font
from pygame.sprite import Group
from ship import Ship
from PyQt5.QtGui import QColor

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
        self.font = pygame.font.SysFont(None, 46)

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
        """Turn the level into a rendered image."""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color)

        # Get the rect and position it
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.top = 8
        self.level_image_rect.left = 210  # Adjust as needed

    def prep_score(self):
        """Turn the score & gold into a rendered image."""
        self.gold_str = str(self.stats.score/4)
        self.score_str = str(self.stats.score)
        self.current_score_str = f"Score: {self.score_str}"
        text_color = (255, 255, 255)
        self.current_score_image = self.font.render(self.current_score_str, True, text_color)
        self.gold_image = self.font.render(self.gold_str, True, text_color)
        
        # Display the gold at the top right of the screen
        self.gold_rect = self.gold_image.get_rect()
        self.gold_rect.right = self.screen_rect.right - 20
        self.gold_rect.top = 20

    def prep_high_score(self):
        """Turn the highest score into a rendered image."""
        high_score_str = f"Highest Score: {self.high_score}"
        
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        # Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx  # Center vertically
        self.high_score_rect.top = 10  # Adjust this value to position it near the top

    def show_score(self):
        """Draw scores to the screen."""
            # current score
        self.screen.blit(self.current_score_image, (1320, 12))
            # gold
        self.screen.blit(self.gold_image, (1800, 17))
            # highest score
        self.screen.blit(self.high_score_image, self.high_score_rect)
            # level
        self.screen.blit(self.level_image, self.level_image_rect)
        
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
