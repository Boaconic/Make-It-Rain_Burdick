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
    w = 1
    
    #primaryWeapon
    
    #def handleCollision(self):
        #pass

    def move(self):
        if self.left:
            self.x -= self.speed
        if self.right:
            self.x += self.speed
        if self.up:
            self.y -= self.speed
        if self.down:
            self.y += self.speed
        self.x = constrain(self.x, self.diameter / 2, width - self.diameter / 2)
        self.y = constrain(self.y, self.diameter / 2, height - self.diameter / 2)
        
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
            
