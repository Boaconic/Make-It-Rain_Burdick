from Sprite import Sprite
import SpriteManager

class Grenade(Sprite):
    
    expandSize = 1
    mark = 0
    wait = 1000
    waitTotal = 5000
    explodeTime = 1000
    diameterX = 50
    diameterY = 50
    c = color(255, 0, 125)
    w = 2
    xSpeed = random(0, 2)
    ySpeed = random(-4, 4)
    
    def move(self):
        
        self.x += self.xSpeed
        self.y += self.ySpeed
        if self.y < 0 or self.y > height:
            self.ySpeed *= -1
        if self.x > width:
            self.xSpeed *= -1
        if self.control() == True:
            self.bounce()
        else:
            self.explode()
            
    def handleCollision(self):
        
        self.w -= 2
        if self.w < 2:
            self.explode()
        elif self.control() == True:
            self.explode()
        else:
            pass
        
    
    def control(self):
        
        if millis() < self.waitTotal:
            return True
        else:
            return False
       
    def bounce(self):
        
        if millis() - self.mark > self.wait:
            self.ySpeed = -self.ySpeed
            self.mark = millis()
    
    def explode(self):
        
        self.w = 2
        
        self.diameterX += 1
        self.diameterY += 1
        self.xSpeed = 0
        self.ySpeed = 0
        self.c = color(255, 165, 0)
        
        if millis() - self.waitTotal < self.explodeTime:
            
            self.diameterX += self.expandSize
            self.diameterY += self.expandSize
            
        else:
            
            SpriteManager.destroy(self)
