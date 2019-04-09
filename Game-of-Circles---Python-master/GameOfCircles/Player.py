import SpriteManager
from Bullet import Bullet
from Sprite import Sprite
from PeaShooter import PeaShooter

class Player(Sprite):
    
    # instance variables
    left = False
    right = False
    up = False
    down = False
    speed = 5
    diameter = 50
    c = color(255,0,0)
    w = 2
    
    
    def __init__(self,x, y, team):
        Sprite.__init__(self, x, y, team)
        self.primaryWeapon = PeaShooter(self)
        
    def fire(self, vector = None):
        if self.hostile:
            if vector is None:
                self.primaryWeapon.shoot(PVector(0, -10))
            else:
                    self.primaryWeapon.shoot(vector)
    
    #def handleCollision(self):
        #pass

    def move(self):
        pass
    
    def playerMover(self):
        pass
        
    def keyDown(self):
        if key == 'f' or key == 'F':
            SpriteManager.spawn(Bullet(self.x, self.y, PVector(0, -10), self.team))
    
        'if keyCode == LEFT:
            self.left = True
        if keyCode == RIGHT:
            self.right = True
        if keyCode == UP:
            self.up = True
        if keyCode == DOWN:
            self.down = True
            
    def keyUp(self):
        if keyCode == LEFT:
            self.left = False
        if keyCode == RIGHT:
            self.right = False
        if keyCode == UP:
            self.up = False
        if keyCode == DOWN:
            self.down = False
            
