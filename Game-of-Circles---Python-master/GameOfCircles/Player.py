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
    diameterX = 50
    diameterY = 50
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
    
    def handleCollision(self):
        pass

    def move(self):
        
        self.x = constrain(self.x, self.diameterX / 2, width - self.diameterX / 2)
        self.y = constrain(self.y, self.diameterY / 2, height - self.diameterY / 2)
        
        if self.left:
            self.x -= 5
        if self.right:
            self.x += 5
        if self.up:
            self.y -= 5
        if self.down:
            self.y += 5
        
    def keyDown(self):
        
        if key == 'f' or key == 'F':
            SpriteManager.spawn(Bullet(self.x, self.y, PVector(0, -10), self.team))
    
        if keyCode == LEFT:
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
            
