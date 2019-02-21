from Sprite import Sprite

class ScreenSaverBot(Sprite):
    
    xspeed = 4
    yspeed = 8
    diameter = 45
    c = color(0,100,255)
        
    def move(self):
        self.y += self.yspeed
        self.x += self.xspeed
        if self.y < 0 or self.y > height:
            self.yspeed *= -1
        if self.x < 0 or self.x > width:
            self.xspeed *= -1
