import SpriteManager
from Bullet import Bullet
from Sprite import Sprite

class Shooter(Sprite):
    mark = 0
    wait = 700
    w = 2
    xspeed = 4
    yspeed = 8
    diameterX = 50
    diameterY = 50
    
    def move(self):
        self.y += self.yspeed
        self.x += self.xspeed
        if self.y < 0 or self.y > height:
            self.yspeed *= -1
        if self.x < 0 or self.x > width:
            self.xspeed *= -1
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
        
    def aim(self, target):
        distance = dist(target.x, target.y, self.x, self.y)
        xComponent = target.x - self.x
        yComponent = target.y - self.y
        if distance == 0: 
            distance = 0.01
        magnitude = 7
        return PVector(xComponent / distance * magnitude, yComponent / distance * magnitude)
            
    def fire(self, vector):
        if millis() - self.mark > self.wait:
            SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
            self.mark = millis()
