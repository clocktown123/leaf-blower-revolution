import pygame
from pygame.math import Vector2
import random
import math

BLUE = (0, 0, 255)

class leaf:
    def __init__(self, xpos, ypos):
        self.x = random.randrange(10, 700)
        self.y = random.randrange(10, 700)
        self.vy = 0
        self.vx = 0
        self.radius = 15
        self.dead = False
        self.leaflvl = 1
        self.leafcost = 500
        self.hasPaid = False
        self.hasUpg = False
        self.cash = 0
        self.range = 70
        self.power = 1

    def draw(self, screen):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), self.radius)
    
    def refresh(self):
        self.dead = False
        self.x = random.randrange(10, 700)
        self.y = random.randrange(10, 700)
        self.hasPaid = False

    def collision(self, mousePos, px, py, cash, pL):

        self.x += self.vx
        self.y += self.vy

        if self.x < 5:
            self.dead = True

        if self.x > 795:
            self.dead = True

        if self.y < 5:
            self.dead = True
            
        if self.y > 795:
            self.dead = True

        #print(self.power)

        if (self.radius+self.range > math.sqrt((px - self.x)**2 + (py - self.y)**2)):

            if px > self.x:
                if py > self.y:
                    #print("The point is in the top-left quadrant.")
                    self.vx, self.vy = -self.power, -self.power
                elif py < self.y:
                    #print("The point is in the bottom-left quadrant.")
                    self.vx, self.vy = -self.power, self.power
            elif px < self.x:
                if py > self.y:
                    #print("The point is in the top-right quadrant.")
                    self.vx, self.vy = self.power, -self.power
                elif py < self.y:
                    #print("The point is in the bottom-right quadrant.")
                    self.vx, self.vy = self.power, self.power

            #self.vx = -self.vx
            #self.vy = -self.vy
        else:
            self.vx = 0
            self.vy = 0
