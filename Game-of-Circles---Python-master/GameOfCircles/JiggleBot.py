from Sprite import Sprite

class JiggleBot(Sprite):
    
    speed = 2
    diameterX = 25
    diameterY = 25
    c = color(125,0,255)
    w = 2
        
    def move(self):
        self.y += random(-self.speed, self.speed)
        self.x += random(-self.speed, self.speed)
        self.y = constrain (self.y, 0, height)
        self.x = constrain (self.x, 0, width)
        
