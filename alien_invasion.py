import sys
import pygame

from alien_invasion_settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from menu import Menu
from scoreboard import Scoreboard

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings=Settings()
        self.stats=GameStats(self)
        self.clock=pygame.time.Clock()
        self.screen=pygame.display.set_mode((self.settings.screen_width, 
                                            self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.game_active=False
        self.menu=Menu(self,"PLAY")
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()
        self.scoreboard=Scoreboard(self)

    def run_game(self):
        while True:
            self._check_events()
            if self.game_active:
                self._update_aliens()
                self.ship.update_pos()
                self._update_bullets()
            self._update_screen()
            self.clock.tick(144)
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.scoreboard.update_hiscore()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4:
                    self.scoreboard.update_hiscore()
                    sys.exit()
                if event.key == pygame.K_d:
                    self.ship.moving_right = True
                elif event.key == pygame.K_a:
                    self.ship.moving_left = True
                if event.key == pygame.K_w:
                    self._fire_bullet()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.ship.moving_right = False
                elif event.key == pygame.K_a:
                    self.ship.moving_left = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self,pos):
        button_clicked=self.menu.button_rect.collidepoint(pos)
        if button_clicked and not self.game_active:
            self.stats.reset_stats()
            self.scoreboard.create_scoreboard()
            self.settings.dynamic_settings()
            self.game_active=True
            self.bullets.remove()
            self.aliens.remove()
            self.scoreboard.create_ship_counter()
            self._create_alien_fleet()
            self.ship.respawn_ship()
            pygame.mouse.set_visible(False)
    
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)
        self._check_bullet_collisions()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.scoreboard.show_score()
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet._draw_bullet()
        self.aliens.draw(self.screen)
        if not self.game_active:
            self.menu.draw_button()
        pygame.display.flip()
    
    def _fire_bullet(self):
        new_bullet=Bullet(self)
        if self.bullets.__len__()<self.settings.maxbullets:
            self.bullets.add(new_bullet)
    
    def _create_alien_fleet(self):
       alien=Alien(self)
       alien_width,alien_height=alien.rect.size
       curr_x,curr_y=alien_width,alien_height
       while curr_y<(self.screen.get_height()-8*alien_height):
        while curr_x<(self.screen.get_width()-2*alien_width):
            self._create_alien(curr_x,curr_y)
            curr_x+=2*alien_width
        curr_x=alien_width
        curr_y+=2*alien_height
    
    def _create_alien(self,x,y):
        new_alien=Alien(self)
        new_alien.x=x
        new_alien.rect.x=x
        new_alien.rect.y=y
        self.aliens.add(new_alien)
    
    def _check_fleet_edges(self):
        if any(alien.check_edge() for alien in self.aliens.sprites()):
                self._change_direction()
    
    def _check_fleet_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom>=self.screen.get_height():
                self._ship_hit()
                break
    
    def _change_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y+=self.settings.fleet_drop
        self.settings.fleet_direction*=-1
            
    def _update_aliens(self):
        self._check_fleet_edges()
        self._check_fleet_bottom()
        self._check_ship_collisions()
        self._respawn_fleet()
        self.aliens.update()

    def _respawn_fleet(self):
        if not self.aliens:
            self._create_alien_fleet()
            self.settings.increase_speed()
            self.scoreboard.increase_lvl()
    
    def _check_bullet_collisions(self):
        collisions=pygame.sprite.groupcollide(self.bullets,self.aliens,True,
                                              True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score+=self.settings.alienpoints*len(aliens)
                self.scoreboard.create_scoreboard()
                self.scoreboard.check_hiscore()

    def _check_ship_collisions(self):
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            print("Mayday! Ship hit!!! GAME OVER")
            self._ship_hit()

    def _ship_hit(self):
        if self.stats.ships>1:
            self.stats.ships-=1
            self.bullets.empty()
            self.aliens.empty()
            self._create_alien_fleet()
            self.ship.respawn_ship()
            sleep(3)
        else:
            self.game_active=False
            pygame.mouse.set_visible(True)

if __name__ == '__main__':
        game=AlienInvasion()
        game.run_game()