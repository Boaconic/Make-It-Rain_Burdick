import SpriteManager
from ArmoredEnemy import ArmoredEnemy
from ScreenSaverBot import ScreenSaverBot

class ArmoredScreenSaverBot(ScreenSaverBot, ArmoredEnemy):
    
    speed = 8
    diameterX = 50
    diameterY = 50
    c = color(255,0,255)
    
    w = 10
