import SpriteManager
from Sprite import Sprite

class BulletCollideTEST(Sprite):
    
    def move(self):
        self.x += self.vector.x
        self.y += self.vector.y
        if(self.x < 0 - self.diameter or self.x > width + self.diameter or self.y < 250 - self.diameter or self.y > height + self.diameter):
            SpriteManager.destroy(self)
