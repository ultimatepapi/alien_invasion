import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:

    def __init__(self,game):
        self.game=game
        self.scoreboard_screen=game.screen
        self.scoreboard_screen_rect=self.scoreboard_screen.get_rect()
        self.settings=game.settings
        self.stats=game.stats
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)
        self.create_scoreboard()
        self.create_hiscore()
        self.create_difficulty_lvl()
        self.create_ship_counter()

    def create_scoreboard(self):
        score=f"SCORE:{round(self.stats.score,-1):,}"
        score_str=str(score)
        self.score_img=self.font.render(score_str,True,self.text_color,
                                        self.settings.bg_color)
        self.score_rect=self.score_img.get_rect()
        self.score_rect.topright=self.scoreboard_screen_rect.topright

    def show_score(self):
        self.scoreboard_screen.blit(self.score_img,self.score_rect)
        self.scoreboard_screen.blit(self.hiscore_img,self.hiscore_rect)
        self.scoreboard_screen.blit(self.lvl_img,self.lvl_rect)
        self.ships.draw(self.scoreboard_screen)

    def create_hiscore(self):
        hiscore=f"HIGHSCORE:{round(self.stats.hiscore,-1):,}"
        hiscore_str=str(hiscore)
        self.hiscore_img=self.font.render(hiscore_str,True,self.text_color,
                                          self.settings.bg_color)
        self.hiscore_rect=self.hiscore_img.get_rect()
        self.hiscore_rect.midtop=self.scoreboard_screen_rect.midtop

    def check_hiscore(self):
        if self.stats.score>self.stats.hiscore:
            self.stats.hiscore=self.stats.score
            self.create_hiscore()
    
    def create_difficulty_lvl(self):
        lvl=f"LEVEL:{self.stats.lvl}"
        lvl_str=str(lvl)
        self.lvl_img=self.font.render(lvl_str,True,self.text_color,
                                      self.settings.bg_color)
        self.lvl_rect=self.lvl_img.get_rect()
        self.lvl_rect.bottomright=self.scoreboard_screen_rect.bottomright

    def increase_lvl(self):
        self.stats.lvl+=1
        self.create_difficulty_lvl()

    def create_ship_counter(self):
        self.ships=Group()
        for ship_no in range(self.stats.ships_left):
            ship=Ship(self.game)
            ship.rect.x=10+ship_no*ship.rect.width
            ship.rect.y=10
            self.ships.add(ship)

    def update_hiscore(self):
        with open('alien_invasion\highscore.txt','r+') as highscore_txt:
            curr_hiscore=int(highscore_txt.read())
            if self.stats.hiscore > curr_hiscore:
                highscore_txt.seek(0)
                highscore_txt.write(str(self.stats.hiscore))

            
            
        