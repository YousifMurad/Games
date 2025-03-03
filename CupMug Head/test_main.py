import pygame
import pygame.sprite
from pygame import mixer
from test_settings import Settings
from test_ship import Ship
from test_bullet import Bullet
from test_alien import Alien
from test_game_stats import GameStats
from test_scoreboard import Scoreboard
from time import sleep
from game_interface import MainWindow as Ui
import sys


class SpaceJet:
    def __init__(self):
        self.column_alien = 2
        self.number_alien_y = self.ui = self.setting = self.screen = self.stats = self.sb = self.ship = self.bullets = self.aliens = None

    def start_ui(self):
        self.ui = Ui(self)
        self.ui.run_ui()

    def run_game(self, name='cup_head'):
        pygame.mixer.init()
        pygame.init()
        # pygame.mixer.music.load('gameConcept/FNF_ Indie Cross - Knockout(MP3_320K).mp3')
        # mixer.music.set_volume(0.1)  # التحكم في الصوت
        # mixer.music.play()

        self.setting = Settings()
        self.stats = GameStats(self)
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.setting.screen_height = self.screen.get_rect().height
        self.setting.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Cup Head game")
        self.sb = Scoreboard(self)
        self.sb.prep_score()
        self.ship = Ship(self, name)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        if self.sb.stats.ships_left <= 0:
            self.screen.blit(self.setting.game_over, (400, 200))
            pygame.quit()
        while True:
            self._check_event()
            if self.stats.game_active:
                self.ship.update()
                #self.bullets.update()
                self._update_bullet()
                self._update_aliens()
            self._update_screen()
            pygame.display.flip()

    def _update_screen(self):
        self.screen.blit(self.setting.background, (0, 0))
        self.screen.blit(self.setting.level_text, (5, 5))
        self.screen.blit(self.setting.coin, (self.setting.screen_width-209, 7))
        self.ship.blitme()
        x = 10
        y = 55
        for soul in range(self.stats.ships_left):
            self.screen.blit(self.setting.souls, (x, y))
            x += 50

        for bullet in self.bullets.sprites():
            bullet.create_bullet()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        pygame.display.flip()

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.K_ESCAPE:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            self.setting.bullet_shot.play()

    def _check_keyup_event(self, event):
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False

    def _fire_bullet(self):
        if len(self.bullets) < self.setting.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        print(len(self.bullets))
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.setting.alien_points * len(aliens)
                self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self.bullets.empty()
            self.column_alien += 1
            self._create_fleet()
            self.setting.increase_speed()
            self.sb.stats.level += 1
            self.sb.prep_level()

    def _create_fleet(self):
        self.row_alien_y = 3
        # self.column_alien
        for row_number in range(self.column_alien):
            for alien_number in range(self.row_alien_y):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.y = alien_height + (alien_height + 20) * alien_number
        alien.rect.y = alien.y
        alien.x = 2299 - alien_width + alien_width * row_number
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def _update_aliens(self):
        #self._check_fleet_edges
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_progress()

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            # self.setting.losing_sound.play()
            sleep(0.2)

        if self.stats.ships_left <= 0:
            self.setting.losing_sound.play()
            self.setting.losing_sound.set_volume(0.08)

            self.screen.blit(self.setting.game_over, (550, 100))
            self.screen.blit(self.setting.losing_image, (1120, 200))
            self.screen.blit(self.setting.losing_phrase, (1150, 170))
            self.sb.blit_score_gold()
            pygame.display.flip()
            sleep(3.2)
            self.stats.game_active = False
            self.ui.show()
            pygame.quit()

    def _check_aliens_progress(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.left <= screen_rect.left:
                self._ship_hit()
                break


if __name__ == '__main__':

    sj = SpaceJet()
    #sj.run_game()
    sj.start_ui()




