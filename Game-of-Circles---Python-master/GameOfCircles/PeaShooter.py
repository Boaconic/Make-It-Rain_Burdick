import SpriteManager
from Pea import Pea

class PeaShooter:
    wait = 400
    mark = 0
    cooldown = True
    
    def __init__(self, handler):
        self.handler = handler
        
    def shoot(self, vector):
        if self.cooldown:
            Pea = Pea(self.handler.x, self.handler.y, vector, self.handler.team)
            SpriteManager.spawn(pea)
            self.cooldown = False
            
        if(millis) - self.mark > self.wait:
            self.mark = millis()
            self.cooldown = True
