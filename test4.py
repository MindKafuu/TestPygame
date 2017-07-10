from __future__ import print_function, division
import pygame
import random
pygame.init()
screen=pygame.display.set_mode((640,480),) 
screenrect = screen.get_rect()

clock = pygame.time.Clock()
mainloop = True
FPS = 30  
radius = 50 
dr = 1  

background = pygame.Surface(screen.get_size())
background.fill((255, 155, 155))     
background = background.convert()
screen.blit(background, (0,0))     

ballsurface = pygame.Surface((50,50))     
ballsurface.set_colorkey((0,0,0))         
pygame.draw.circle(ballsurface, (100,175,81), (25,25),25) 
ballsurface = ballsurface.convert_alpha()       
ballrect = ballsurface.get_rect() 
ballx, bally = 550, 240           
dx = 10                            
dy = 0                 

x1 = 50
y1 = 200
dx1 = 7
dy1 = 0
radius1 = 40

pygame.draw.circle(background, (0,0,200), (screenrect.width//2, screenrect.height//2), screenrect.width//3)

while mainloop:
    milliseconds = clock.tick(FPS) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False 
    pygame.display.set_caption("Test")
    screen.blit(background, (0,0))
    
    x1 += dx1
    if x1 + radius1 >= screenrect.width:
        x1 = screenrect.width - radius1
        dx1 *= -1
    elif x1 - radius1 <= 0:
        x1 =  radius1
        dx1 *= -1
    pygame.draw.circle(screen, (255,255,0), (x1,y1), radius1)

    ballx += dx
    bally += dy 
    if ballx < 0: 
        ballx = 0
        dx *= -1 
    elif ballx + ballrect.width > screenrect.width:
        ballx = screenrect.width - ballrect.width
        dx *= -1
    screen.blit(ballsurface, (round(ballx,0), round(bally,0)))    

    colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    if radius >100 or radius < 5:
        dr *= -1
    radius += dr
    pygame.draw.circle(screen, colour , (100,100), radius, 2) 
 
    pygame.display.flip()          
pygame.quit()


