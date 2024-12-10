import pygame
import random
from leafblower import player
from Leaf import leaf

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("leaf blower")
clock = pygame.time.Clock() # controls frame rates

#direction
A = 0
D = 1
W = 2
S = 3
direct = [False, False, False, False]

#leaf positions
leafX = random.randrange(0, 800)
leafY = random.randrange(0, 800)

#classes
p1 = player()
l1 = leaf(leafX, leafY)

cash = 0

state = 1

#state bottons
button1 = False
button2 = False

#mouse x pos and y pos
mxpos = 0
mypos = 0

mousePos = (mxpos, mypos)
mouseDown = False

#other variables
amount = 30

last_check_time = pygame.time.get_ticks()

text_font = pygame.font.SysFont("Sans", 60, bold = True)

def draw_text(text, font, text_col, tx, ty):
    img = font.render(text, True, text_col)
    screen.blit(img, (tx, ty))

leafBag = []
for i in range(amount):
    leafBag.append(leaf(leafX, leafY))

while 1:
    clock.tick(60)

    #input section-------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        
    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos

        if mousePos[0] > p1.pos.x:
            #p1.vx = 5
            direct[D] = True
        elif mousePos[0] < p1.pos.x:
            #p1.vx = -5
            direct[A] = True
        #else:
            #p1.vx = 0
                
        if mousePos[1] > p1.pos.y:
            #p1.vy = 5
            direct[S] == True
        elif mousePos[0] < p1.pos.y:
            #p1.vy = -5
            direct[W] == True
        #else:
           # p1.vy = 0

    #keeps track of mouse button
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouseDown = True
    if event.type == pygame.MOUSEBUTTONUP:
        mouseDown = False
    
    p1.pos.x += p1.vx
    p1.pos.y += p1.vy


    #physics section----------------------------------------------------------------------------------------

    for i in range(len(leafBag)):
            leafBag[i].collision(mousePos, p1.pos.x, p1.pos.y)

    current_time = pygame.time.get_ticks()
    if current_time - last_check_time >= 15000:  # 15 seconds in milliseconds
        # Do your thing here
        print("all leaves respawn")
        for i in range(len(leafBag)):
            if leafBag[i].dead == True:
                leafBag[i].refresh()

        # Reset the timer
        last_check_time = current_time

    p1.move(direct)
    
    #states--------------------------------------------------------------------------------------------------
    if state == 1 and mousePos[0]>300 and mousePos[0]<500 and mousePos[1]>300 and mousePos[1]<450:
        button1 = True
    else:
        button1 = False

    if state == 1 and button1 == True and mouseDown == True:
        state = 2
    #render section------------------------------------------------------------------------------------------
    if state == 1:
        screen.fill((230,100,100))# Clear the screen pink

        if button1 == False:
            pygame.draw.rect(screen, (100, 230, 100), (300, 300, 200, 150))
        else:
            pygame.draw.rect(screen, (200, 250, 200), (300, 300, 200, 150))


        draw_text("Leaf Blower Revolution", text_font, (0,0,0), 100, 50)
        draw_text("Start", text_font, (0,0,0), 330, 350)
        
    elif state == 2:
        screen.fill((128,255,128))

        p1.pos.x,p1.pos.y = pygame.mouse.get_pos()

        for i in range(len(leafBag)):
            if leafBag[i].dead == False:
                leafBag[i].draw(screen)

        p1.draw(screen)

        
    pygame.display.flip()#this actually puts the pixel on the screen
