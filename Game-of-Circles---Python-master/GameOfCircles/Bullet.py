import SpriteManager
from Sprite import Sprite
from BulletCollideTEST import BulletCollideTEST

class Bullet(BulletCollideTEST):
    
    diameter = 10
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
        
    #def PlayerMove(self):
        if(self.x < 0 - self.diameter or self.x > width + self.diameter or self.y < 0 - self.diameter or self.y > height + self.diameter):
            SpriteManager.destroy(self)
            
    def handleCollision(self):
        self.w -= 2
        if self.w < 2:
            SpriteManager.destroy(self)
        
