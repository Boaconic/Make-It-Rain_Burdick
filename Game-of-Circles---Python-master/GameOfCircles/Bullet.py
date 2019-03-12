import SpriteManager
from Sprite import Sprite

class Bullet(Sprite):
    
    diameter = 10
    c = color(0)
    
    w = 1
    
    def __init__(self, x, y, vector, team):
        self.x = x
        self.y = y
        self.vector = vector
        self.team = team
        
        if self.x < -10 or self.x > width + 10 or self.y < -10 or self.y > height + 10:
            SpriteManager.destroy(self)
        
    def move(self):
        self.x += self.vector.x
        self.y += self.vector.y
