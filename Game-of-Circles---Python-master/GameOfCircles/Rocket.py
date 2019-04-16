from Sprite import Sprite

def Rocket(Sprite):
    
    def move(self):
    
    
    
    def aim(self, target):
        distance = dist(target.x, target.y, self.x, self.y)
        xComponent = target.x - self.x
        yComponent = target.y - self.y
        if distance == 0: 
            distance = 0.01
        magnitude = 7
        return PVector(xComponent / distance * magnitude, yComponent / distance * magnitude)
