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
from ArmoredJiggleBot import ArmoredJiggleBot
from Rocket import Rocket

def setup():
    
    enemyNumber = int(random(1,5))
    
    a = Enemy
    b = Raindrop
    c = JiggleBot
    d = ScreenSaverBot
    e = Lobber
    f = Shooter
    g = ArmoredEnemy
    h = ArmoredShooter
    i = ArmoredScreenSaverBot
    j = ArmoredLobber
    k = ArmoredJiggleBot
    
    enemies = [a, b, c, d, e, f, g, h, i, j, k] 
    print "Built with Processing Python version " + platform.python_version()
    size(500, 500)
    player = Player(width / 2, height / 2, 1)
    SpriteManager.setPlayer(player)
    #SpriteManager.spawn(ScreenSaverBot(random(0, height), 50, 2))
    SpriteManager.spawn(Rocket(0, random(0, height), 3))
    
    #for i in range (0, enemyNumber):
        #SpriteManager.spawn(enemies[int(random(0, len(enemies)))](random(0, width), 50, 2))
    
def draw():
    background(255)    
    SpriteManager.animate()
        
def keyPressed():
    SpriteManager.player.keyDown()
        
def keyReleased():
    SpriteManager.player.keyUp()
