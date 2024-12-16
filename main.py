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
button3 = False
button4 = False
button5 = False


#mouse x pos and y pos
mxpos = 0
mypos = 0

mousePos = (mxpos, mypos)
mouseDown = False

#COLORS
DGREEN = (0, 102, 0)
GREEN = (128,255,128)
LGREEN = (76, 153, 0)

RED = (153, 0, 0)
LRED = (204, 0 , 0)

ORANGE = (204, 102, 0)
LORANGE = (255, 128, 0)

BLUE = (51, 153, 255)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#other variables
amount = 50
hasPaid = False

last_check_time = pygame.time.get_ticks()
last_upg_check_time = pygame.time.get_ticks()

text_font = pygame.font.SysFont("Sans", 60, bold = True)
smol_text_font = pygame.font.SysFont("Sans", 30, bold = True)

def draw_text(text, font, text_col, tx, ty):
    img = font.render(text, True, text_col)
    screen.blit(img, (tx, ty))

leafBag = []
for i in range(amount):
    leafBag.append(leaf(leafX, leafY))

upgrade_leaves = []


def better_round(val:float, n_digits:int = 0):
    val *= 10**n_digits
    result = int(val + (0.5 if val >= 0 else -0.5))
    return result / 10**n_digits


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
        leafBag[i].collision(mousePos, p1.pos.x, p1.pos.y, cash, p1.level)

    current_time = pygame.time.get_ticks()
    if current_time - last_check_time >= 10000:  # 10 seconds in milliseconds
        # Do your thing here
        print("all leaves respawn")
        for i in range(len(leafBag)):
            if leafBag[i].dead == True:
                leafBag[i].refresh()

        # Reset the timer
        last_check_time = current_time

    p1.move(direct)

    cashMulti = leafBag[i].leaflvl**2

    for i in range(len(leafBag)):
        if leafBag[i].dead == True and leafBag[i].hasPaid == False:
            cash += 5*cashMulti
            leafBag[i].hasPaid = True
            
    current_upg_time = pygame.time.get_ticks()
    if current_upg_time - last_upg_check_time >= 1500:  # 1.5 seconds in milliseconds
        p1.hasUpg = False
        leafBag[i].hasUpg = False

        last_upg_check_time = current_upg_time
    
    #UPGRADES-----------------------------------------------------------------------------------------------

    #BLOWER

    if state == 3 and mousePos[0]>150 and mousePos[0]<350 and mousePos[1]>300 and mousePos[1]<500:
        button4 = True
    else:
        button4 = False

    if button4 == True and mouseDown == True and p1.hasUpg == False and cash >= p1.cost:
        p1.hasUpg = True
        cash -= p1.cost
        p1.level += 1
        p1.cost *= 1.5
        for i in range(len(leafBag)):
            leafBag[i].range *= 1.5
            leafBag[i].power *= 1.5

    leafBag[i].range = better_round(leafBag[i].range)
    leafBag[i].power = better_round(leafBag[i].power)
        
    #print(mousePos[0], mousePos[1])
    #print(leafBag[i].range)

    #LEAF

    if state == 3 and mousePos[0]>400 and mousePos[0]<600 and mousePos[1]>300 and mousePos[1]<500:
        button5 = True
    else:
        button5 = False

    if button5 == True and mouseDown == True and leafBag[i].hasUpg == False and cash >= leafBag[i].leafcost:
        leafBag[i].hasUpg = True
        cash -= leafBag[i].leafcost
        leafBag[i].leaflvl += 1
        leafBag[i].leafcost *= 2
        

    print(len(leafBag))
    
    #states--------------------------------------------------------------------------------------------------
    
    #state 1#############################
    if state == 1:
        if mousePos[0]>300 and mousePos[0]<500 and mousePos[1]>300 and mousePos[1]<450:
            button1 = True
        else:
            button1 = False

        if button1 == True and mouseDown == True:
            state = 2
    
    #state 2#############################
    elif state == 2:
        if mousePos[0]>50 and mousePos[0]<150 and mousePos[1]>75 and mousePos[1]<175:
            button2 = True
        else:
            button2 = False
        

        if  button2 == True and mouseDown == True:
            state = 3
    
    #state 3###############################
    elif state == 3:
        if mousePos[0]>25 and mousePos[0]<125 and mousePos[1]>25 and mousePos[1]<75:
            button3 = True
        else:
            button3 = False
        

        if  button3 == True and mouseDown == True:
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


        #upgrades section
        if button2 == False:
            pygame.draw.rect(screen, (DGREEN), (50, 75, 100, 100))
            pygame.draw.rect(screen, (BLACK), (50, 75, 100, 100), 5)
        else:
            pygame.draw.rect(screen, (LGREEN), (50, 75, 100, 100))
            pygame.draw.rect(screen, (BLACK), (50, 75, 100, 100), 5)

        draw_text("UPGR", smol_text_font, (0,0,0), 65, 95)
        draw_text("ADES", smol_text_font, (0,0,0), 65, 125)


        #money
        draw_text("$: ",  text_font, (BLACK), 25, 730)
        draw_text(str(int(cash)),  text_font, (BLACK), 85, 730)

        for i in range(len(leafBag)):
            if leafBag[i].dead == False:
                leafBag[i].draw(screen)

        p1.draw(screen)

    elif state == 3:
        screen.fill((BLUE))

        draw_text("$: ",  text_font, (BLACK), 25, 730)
        draw_text(str(int(cash)),  text_font, (BLACK), 85, 730)

        #EXIT BUTTON############################################################
        if button3 == False:
            pygame.draw.rect(screen, (RED), (25, 25, 100, 50))
            pygame.draw.rect(screen, (BLACK), (25, 25, 100, 50), 5)
        else:
            pygame.draw.rect(screen, (LRED), (25, 25, 100, 50))
            pygame.draw.rect(screen, (BLACK), (25, 25, 100, 50), 5)

        draw_text("x",  text_font, (BLACK), 63, 11)

        #LEAF BLOWER UPGRADE#########################################################
        if button4 == False:
            pygame.draw.rect(screen, (ORANGE), (150, 300, 200, 200))
            pygame.draw.rect(screen, (BLACK), (150, 300, 200, 200), 5)
        else:
            pygame.draw.rect(screen, (LORANGE), (150, 300, 200, 200))
            pygame.draw.rect(screen, (BLACK), (150, 300, 200, 200), 5)

        draw_text("BLOWER COST:",  smol_text_font, (BLACK), 155, 300)
        draw_text(str(int(p1.cost)),  smol_text_font, (BLACK), 230, 350)
        draw_text("BLOWER LVL: ",  smol_text_font, (BLACK), 170, 400)
        draw_text(str(p1.level),  smol_text_font, (BLACK), 240, 440)

        #LEAF UPGRADE###################################################################
        
        if button5 == False:
            pygame.draw.rect(screen, (DGREEN), (400, 300, 200, 200))
            pygame.draw.rect(screen, (BLACK), (400, 300, 200, 200), 5)
        else:
            pygame.draw.rect(screen, (LGREEN), (400, 300, 200, 200))
            pygame.draw.rect(screen, (BLACK), (400, 300, 200, 200), 5)
        
        draw_text("LEAF COST: ",  smol_text_font, (BLACK), 430, 300)
        draw_text(str(int(leafBag[i].leafcost)),  smol_text_font, (BLACK), 475, 350)
        draw_text("LEAF LVL: ",  smol_text_font, (BLACK), 435, 400)
        draw_text(str(leafBag[i].leaflvl),  smol_text_font, (BLACK), 490, 440)

        
    pygame.display.flip()#this actually puts the pixel on the screen
