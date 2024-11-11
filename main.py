import pygame
import random
from leafblower import player
from Leaf import leaf

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("leaf blower")
clock = pygame.time.Clock() # controls frame rates


A = 0
D = 1
W = 2
S = 3
keys = [False, False, False, False]

p1 = player()
l1 = leaf()

state = 1

button1 = False
button2 = False

mxpos = 0
mypos = 0

mousePos = (mxpos, mypos)
mouseDown = False

text_font = pygame.font.SysFont("Sans", 60, bold = True)

def draw_text(text, font, text_col, tx, ty):
    img = font.render(text, True, text_col)
    screen.blit(img, (tx, ty))


while 1:
    clock.tick(60)

    #input section-------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                keys[A] = True
                #RowNum = 0
            if event.key == pygame.K_d:
                keys[D] = True
                #RowNum = 3
            if event.key == pygame.K_w:
                keys[W] = True
                #RowNum = 1
            if event.key == pygame.K_s:
                keys[S] = True

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_a:
                keys[A] = False
                #RowNum = 0
            if event.key == pygame.K_d:
                keys[D] = False
                #RowNum = 3
            if event.key == pygame.K_w:
                keys[W] = False
                #RowNum = 1
            if event.key == pygame.K_s:
                keys[S] = False
        
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
        #keeps track of mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False

    #physics section----------------------------------------------------------------------------------------

    p1.move(keys)
        
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

        for i in range(50):
            l1.draw(screen)


        p1.draw(screen)

        
    pygame.display.flip()#this actually puts the pixel on the screen
