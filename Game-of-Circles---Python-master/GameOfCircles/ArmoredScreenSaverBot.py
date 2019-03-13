import SpriteManager
from Sprite import Sprite
from ArmoredEnemy import ArmoredEnemy
from ScreenSaverBot import ScreenSaverBot

class ArmoredScreenSaverBot(ScreenSaverBot, ArmoredEnemy):
    
    speed = 8
    diameter = 50
    c = color(255,0,255)
    
    w = 10
