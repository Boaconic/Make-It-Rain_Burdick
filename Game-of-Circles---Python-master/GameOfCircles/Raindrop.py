from Sprite import Sprite

class Raindrop(Sprite):
    
    speed = 8
    diameter = 15
    c = color(0,0,255)
    
    def move(self):
        self.y += self.speed
        if self.y < 0 or self.x > width:
            self.speed *= -1
        if self.y > 500:
            self.y = 0
