import SpriteManager
from Sprite import Sprite

class ArmoredEnemy(Sprite):
    
    speed = 8
    diameter = 50
    c = color(255,0,255)
    
    w = 10
    
    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
            
    def handleCollision(self):
        self.w -= 2
        if self.w < 2:
            SpriteManager.destroy(self)
