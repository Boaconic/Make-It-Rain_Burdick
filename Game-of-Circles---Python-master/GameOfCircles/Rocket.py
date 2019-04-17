from Sprite import Sprite
import SpriteManager

class Rocket(Sprite):
    
    mark = 0
    wait = 1000
    seconds =[1, 2, 3, 4]
    diameterX = 75
    diameterY = 25
    c = color(255, 0, 125)
    w = 2
    xSpeed = random(0, 4)
    ySpeed = random(-4, 4)
    
    def move(self):
        
        for x in self.seconds:
            if millis() - self.mark < self.wait:
                self.x += self.xSpeed
                self.y += -self.ySpeed
                self.mark += millis()
            
