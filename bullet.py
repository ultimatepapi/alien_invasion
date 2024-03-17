import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen=game.screen
        self.settings=game.settings
        self.color=self.settings.bulletcolor
        self.rect=pygame.Rect(0,0,self.settings.bulletwidth,
                              self.settings.bulletheight)
        self.rect.midtop=game.ship.rect.midtop
        self.y=float(self.rect.y)

    def update(self):
        self.y-=self.settings.bulletspeed
        self.rect.y=self.y

    def _draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
