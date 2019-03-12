import SpriteManager 
from Sprite import Sprite
from Bullet import Bullet
from Player import Player

class Lobber(Sprite):
    
    

    yspeed = 4
    xspeed = 8
    diameter = 50
    c = color(0,0,255)
    w = 1

    def move(self):
        vector = self.aim(SpriteManager.getPlayer())
        self.y += self.yspeed
        self.x += self.xspeed
        if self.y < 0 or self.y > height:
            self.yspeed *= -1
            self.fire(vector)
        if self.x < 0 or self.x > width:
            self.xspeed *= -1
            
        #mark = 0
        #wait = 1000
        #go = True      
            
        #if(millis() - mark  > wait):
            #go = not go
            #mark = millis()
            
        #if (go):
            
            self.fire(vector)
        #else:
            #c = color(255, 0, 255)
        
    def aim(self, target):
        xComponent = target.x - self.x
        yComponent = target.y - self.y
        d = sqrt((xComponent * xComponent) - (yComponent * yComponent))
        xVector = xComponent / d
        yVector = yComponent / d
        
        return PVector(xVector, yVector)
    
    def fire(self, vector):
        SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
