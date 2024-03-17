class GameStats:
    def __init__(self,game):
        self.settings=game.settings
        self.reset_stats()
        self.score=0
        with open('alien_invasion\highscore.txt','r') as highscore_txt:
            self.hiscore=int(highscore_txt.read())
        self.lvl=1
        
    def reset_stats(self):
        self.ships_left=self.settings.ships_left
        self.score=0