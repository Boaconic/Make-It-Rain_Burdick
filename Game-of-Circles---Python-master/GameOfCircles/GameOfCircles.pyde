import platform
import SpriteManager
from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from SpriteManager import sprites
from Raindrop import Raindrop
from JiggleBot import JiggleBot
from ScreenSaverBot import ScreenSaverBot
from Lobber import Lobber

def setup():
    print "Built with Processing Python version " + platform.python_version()
    size(500, 500)
    player = Player(width / 2, height - 100, 1)
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(ScreenSaverBot(random(0, width), 50, 2))
    SpriteManager.spawn(Lobber(random(0, width), 50, 2))
    
def draw():
    background(255)    
    SpriteManager.animate()
        
def keyPressed():
    SpriteManager.player.keyDown()
        
def keyReleased():
    SpriteManager.player.keyUp()
