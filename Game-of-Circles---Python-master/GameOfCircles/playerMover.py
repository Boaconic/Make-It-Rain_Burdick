from Sprite import Sprite

class playerMover(Sprite):
    
    def playerMove():
        
        if self.left:
            self.x += 5
        if self.right:
            self.x -= 5
        if self.up:
            self.y += 5
        if self.down:
            self.y -= 5
            
    def keyDown(self):
        
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
