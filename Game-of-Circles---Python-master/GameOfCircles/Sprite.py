import SpriteManager

class Sprite(object):
    diameterX = 50
    diameterY = 50
    c = color(0, 255, 0)
    
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    def move():
        pass
        
        
    def display(self):
        fill(self.c)
        strokeWeight(self.w)
        ellipse(self.x, self.y, self.diameterX, self.diameterY)
        
    def animate(self):
        
        self.move()
        self.display()
        
    def isColliding(self, other):
        r1 = self.diameterX / 2.0
        r2 = other.diameterX / 2.0
        if r1 + r2 > dist(self.x, self.y, other.x, other.y):
            return True
        else:
            return False
    
    def handleCollision(self):
        self.w -= 2
        if self.w < 2:
            SpriteManager.destroy(self)
