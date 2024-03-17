import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen=game.screen
        self.settings=game.settings
        self.screen_rect=game.screen.get_rect()
        self.image=pygame.image.load('alien_invasion\ship.bmp').convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)
        self.moving_right=False
        self.moving_left=False
    
    def update_pos(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def respawn_ship(self):
        self.rect=self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom