import pygame

class Roket_class():
    """description of class"""
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("images/rocket.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False


         
    def bliteme(self):
        #在指定位置绘制火箭
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.move_up :
            if self.rect.top>0:
                self.rect.centery-=1
        if self.move_down:
            if self.rect.bottom<self.screen_rect.bottom:
                self.rect.centery+=1
        if self.move_left:
            if self.rect.left>0:
                self.rect.centerx-=1
        if self.move_right:
            if self.rect.right<self.screen_rect.right:
                self.rect.centerx+=1