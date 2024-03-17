class Settings:

    def __init__(self):
        #screensettings
        self.screen_width=1920
        self.screen_height=1080
        self.bg_color=(230,230,230)

        #bullet
        self.bulletwidth=3
        self.bulletheight=15
        self.bulletcolor=(60,60,60)
        self.maxbullets=3.5

        #aliens
        self.fleet_drop=5

        #ships
        self.ships_left=3

        #difficulty scale
        self.speed_up=1.2

        self.dynamic_settings()

    def dynamic_settings(self):
        self.ship_speed=1.5
        self.alienspeed=1.0
        self.fleet_direction=1
        self.bulletspeed=10
        self.alienpoints=50

    def increase_speed(self):
        self.ship_speed*=self.speed_up
        self.alienspeed*=self.speed_up
        self.bulletspeed*=self.speed_up
        self.alienpoints*=self.speed_up