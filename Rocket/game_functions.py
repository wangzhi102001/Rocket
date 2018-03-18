import pygame
import sys
from roket_class import Roket_class
def check_events(rockrt):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rockrt.move_left = True
            if event.key == pygame.K_RIGHT:
                rockrt.move_right = True
            if event.key == pygame.K_UP:
                rockrt.move_up = True
            if event.key == pygame.K_DOWN:
                rockrt.move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                rockrt.move_left = False
            if event.key == pygame.K_RIGHT:
                rockrt.move_right = False
            if event.key == pygame.K_UP:
                rockrt.move_up = False
            if event.key == pygame.K_DOWN:
                rockrt.move_down = False







    
