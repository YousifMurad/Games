class GameStats:

    def __init__(self, s_game):
        self.ships_left = self.score = self.level = None
        self.setting = s_game.setting
        self.reset_stats()
        self.game_active = True
        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.setting.ship_limit
        self.score = 0
        self.level = 1
