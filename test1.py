import os, random, math, time
import pygame

pygame.init()
screen_width  = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("tatemono")

clock = pygame.time.Clock()
the_black = pygame.image.load("images/black.png")

running = True

class BACKGROUND(pygame.sprite.Sprite):
    def __init__(self, position=(400, 300)):
        super().__init__()
        self.image = pygame.image.load("images/background3.png").convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.rect.center = (400, 300)
        self.mask = pygame.mask.from_surface(self.image)
        
background = BACKGROUND()

while running:
    clock.tick(60)
    screen.blit(the_black, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("스페이스바 눌림")
                
            if event.key == pygame.K_LEFT:
                print("왼쪽키 눌림")                

            if event.key == pygame.K_1:
               print("1 눌림")
            if event.key == pygame.K_2:
                print("2 눌림")
            if event.key == pygame.K_3:
                print("3 눌림")
            if event.key == pygame.K_6:
                print("6 눌림")
            if event.key == pygame.K_8:
                print("8 눌림 (아마)")
             
         
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                time.sleep(0)
   
    background.mask = pygame.mask.from_surface(background.image)
    pygame.display.update()

pygame.time.delay(3000)
pygame.quit()