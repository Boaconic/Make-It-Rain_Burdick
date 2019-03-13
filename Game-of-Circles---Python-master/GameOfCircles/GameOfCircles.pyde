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
from Shooter import Shooter
from ArmoredEnemy import ArmoredEnemy
from ArmoredShooter import ArmoredShooter
from ArmoredScreenSaverBot import ArmoredScreenSaverBot
from ArmoredLobber import ArmoredLobber

def setup():
    print "Built with Processing Python version " + platform.python_version()
    size(500, 500)
    player = Player(width / 2, height - 100, 1)
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(Shooter(random(0, width), 50, 2))
    SpriteManager.spawn(ArmoredLobber(random(0, width), 50, 2))
    
def draw():
    background(255)    
    SpriteManager.animate()
        
def keyPressed():
    SpriteManager.player.keyDown()
        
def keyReleased():
    SpriteManager.player.keyUp()
