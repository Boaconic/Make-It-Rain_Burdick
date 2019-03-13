import SpriteManager
from Sprite import Sprite
from ArmoredEnemy import ArmoredEnemy
from Shooter import Shooter

class ArmoredShooter(ArmoredEnemy, Shooter):
    
    xspeed = 4
    yspeed = 8
    
    c = color(255, 0, 255)
    
    def move(self):
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
        self.y += self.yspeed
        self.x += self.xspeed
        if self.y < -75 or self.y > height+75:
            self.yspeed *= -1
        if self.x < -75 or self.x > width+75:
            self.xspeed *= -1
