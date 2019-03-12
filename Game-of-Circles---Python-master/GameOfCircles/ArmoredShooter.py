import SpriteManager
from Sprite import Sprite
from ArmoredEnemy import ArmoredEnemy
from Shooter import Shooter

class ArmoredShooter(ArmoredEnemy, Shooter):
    
    xspeed = 4
    yspeed = 8
    
    def move(self):
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
        self.y += self.yspeed
        self.x += self.xspeed
        if self.y < 0 or self.y > height:
            self.yspeed *= -1
        if self.x < 0 or self.x > width:
            self.xspeed *= -1
