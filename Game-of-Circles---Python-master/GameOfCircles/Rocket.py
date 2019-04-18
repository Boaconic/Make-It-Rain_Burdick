from Sprite import Sprite
import SpriteManager

class Rocket(Sprite):
    
    mark = 0
    wait = 1000
    waitTotal = 4000
    diameterX = 75
    diameterY = 25
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
        if self.control() == True:
            self.explode
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
        
        self.diameterX = 25
        self.diameterY = 25
        self.xSpeed = 0
        self.ySpeed = 0
        self.c = color(255, 165, 0)
