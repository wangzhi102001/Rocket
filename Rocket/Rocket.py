import pygame
import sys
from roket_class import Roket_class
import game_functions as gf

def run_game():
    pygame.init()
    
    screen = pygame.display.set_mode((800,600)) #创建窗体对象，设置属性大小为800*600
    pygame.display.set_caption("RocketGame")
    
    Rocket = Roket_class(screen)
    
    
    while True:
        screen.fill((230,230,230))
        Rocket.bliteme()
        gf.check_events(Rocket)
        Rocket.update()
        pygame.display.flip()
    


run_game()




