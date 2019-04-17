import SpriteManager
from Sprite import Sprite

class ArmoredEnemy(Sprite):
    
    speed = 4
    diameterX = 50
    diameterY = 50
    c = color(0,0,255)
    
    w = 10
    
    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
            
    #def handleCollision(self):
        
            #SpriteManager.destroy(self)
