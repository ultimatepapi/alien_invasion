import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen=game.screen
        self.settings=game.settings
        self.screen_rect=game.screen.get_rect()
        self.image=pygame.image.load('alien_invasion\lien.bmp').convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.topleft=self.screen_rect.topleft
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
    
    def update(self):
        self.x+=self.settings.alienspeed*self.settings.fleet_direction
        self.rect.x=self.x
    
    def check_edge(self):
        screen_rect=self.screen.get_rect()
        return (self.rect.right>=screen_rect.right) or (self.rect.left<=0)