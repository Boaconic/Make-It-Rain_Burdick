from Sprite import Sprite

class Lobber(Sprite):
    
    speed = 8
    diameter = 50
    c = color(0,0,255)

    def move(self):
        self.y += self.yspeed
        self.x += self.xspeed
        if self.y < 0 or self.y > height:
            self.yspeed *= -1
        if self.x < 0 or self.x > width:
            self.xspeed *= -1
            
    def aim():
        
