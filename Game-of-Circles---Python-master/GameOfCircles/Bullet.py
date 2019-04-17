import SpriteManager
from Sprite import Sprite
from BulletCollideTEST import BulletCollideTEST

class Bullet(BulletCollideTEST):
    
    diameterX = 10
    diameterY = 10
    c = color(0)
    
    w = 2
    
    def __init__(self, x, y, vector, team):
        self.x = x
        self.y = y
        self.vector = vector
        self.team = team
        
    def move(self):
        self.x += self.vector.x
        self.y += self.vector.y
        
        if(self.x < 0 - self.diameterX or self.x > width + self.diameterX or self.y < 0 - self.diameterY or self.y > height + self.diameterY):
            SpriteManager.destroy(self)
            
    def handleCollision(self):
        self.w -= 2
        if self.w < 2:
            SpriteManager.destroy(self)
        
