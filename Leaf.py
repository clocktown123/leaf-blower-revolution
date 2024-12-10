import pygame
import math #needed for square root function

pygame.init()

screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption("air hockey")

doExit = False

clock = pygame.time.Clock()

#striker = pygame.transform.scale(pygame.image.load('Striker.png'), (80, 80))
#Background = pygame.image.load('AirHockeyRink.png')

p1x = 20
p1y = 200

p2x = 750
p2y = 200

#ball variables
bx = 350 #xposition
by = 250 #yposition
bVx = 3 #x velocity (horizontal speed)
bVy = 3 #y velocity (vertical speed)

Vx = 1
Vy = 1


#ball variables
bx = 350 #xposition
by = 250 #yposition
bVx = 5 #x velocity (horizontal speed)
bVy = 5 #y velocity (vertical speed)

p2Score = 0
p1Score = 0

while not doExit: #Game Loop
    
    #event que stuff
    clock.tick(60) #set the fps

    for event in pygame.event.get(): #check if user did something
        if event.type == pygame.QUIT: #check if user clicked close
            doExit = True #flag that e are done so we exit game loop
            
    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos
        
        if (mousePos[0] > p1x):
            Vx = 5
        else:
            Vx = -5
        if (mousePos[1] > p1y):
            Vy = 5
        else:
            Vy = -5
        
    #scoring system
            
    if bx < 5:
        p2Score += 1
        
    if bx > 970:
        p1Score += 1
            
#physics section------------------------------------
    #update circle position
    p1x += Vx
    p1y += Vy
    
    
    #SKYNET
    if p2y < by:
        p2y+=5
    else:
        p2y-=5

    #if p2x < bx:
        #p2x+=5
    #else:
        #p2x-=5
        
    #ball movement
    bx += bVx
    by += bVy
        
    #reflect the ball off side walls of screen
    if bx < 0 or bx + 30 > 1000:
            bVx *= -1
    if by > 500 - 30 or by < 0:
            bVy *= -1
    #Puck and striker collison
            
    if (40+30 > math.sqrt((p1x - bx)**2 + (p1y - by)**2)):
        print("collision")
        bVx = -bVx*1
        bVy = -bVy*1
        
    if (40+30 > math.sqrt((p2x - bx)**2 + (p2y - by)**2)):
        print("collision")
        bVx = -bVx*1
        bVy = -bVx*1
        
    
#render section--------------------------------------
    screen.fill((0,0,0)) #wipe screen (without this, things smear)
    p1x,p1y = pygame.mouse.get_pos()
    
    #screen.blit(Background, (0,0), (0,0, 1000, 500))
    
    #Strikers
    pygame.draw.circle(screen, (150, 0, 0), (p1x, p1y), 40)
    pygame.draw.circle(screen, (150, 0, 0), (p2x, p2y), 40)
    
    #screen.blit(striker, (p1x-40, p1y-40))
    #screen.blit(striker, (p2x-40, p2y-40))
    #puck
    pygame.draw.circle(screen, (150, 110, 250), (bx, by), 30)
    
    font = pygame.font.Font(None, 74)
    text = font.render(str(p1Score), 1, (255, 255, 255))
    screen.blit(text, (50,10))
    text = font.render(str(p2Score), 1, (255, 255, 255))
    screen.blit(text, (910,10))
    
    pygame.display.flip()
    
#end game loop------------------------------------------
    
pygame.quit()
    
