import pygame
from pygame.math import Vector2
import math

A = 0
D = 1
W = 2
S = 3
direct = [False, False, False, False]

class player:
    def __init__ (self):
        self.pos = Vector2(200,615)
        self.vx=0
        self.vy=0
        self.direction = D
        self.level = 1
        self.cost = 250
        self.hasUpg = False
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,0,255), (self.pos.x, self.pos.y), 50)
    
    def move(self, direct):
        if direct[A] == True:
            self.vx = -3
            self.direction = A
        elif direct[D] == True:
            self.vx = 3
            self.direction = D
        else:
            self.vx = 0

        if direct[W] == True:
            self.vy = -3
            self.direction = W
        elif direct[S] == True:
            self.vy = 3
            self.direction = S
        else:
            self.vy = 0
        
        self.pos.y += self.vy
        self.pos.x += self.vx
    
    #def collision(self, mousePos, lvx, lvy, radius):
        #if math.sqrt((mousePos[0]  - lvx)**2 + (mousePos[1] - lvy)**2)<radius:
            #print("collision")
            #lvx *= -1
            #lvy *= -1
