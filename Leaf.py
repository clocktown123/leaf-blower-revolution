import pygame
from pygame.math import Vector2
import random
import math

BLUE = (0, 0, 255)

class leaf:
    def __init__(self, xpos, ypos):
        self.x = random.randrange(0, 700)
        self.y = random.randrange(0, 700)
        self.vy = 0
        self.vx = 0
        self.radius = 15
        self.dead = False

    def draw(self, screen):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), self.radius)
    
    #def move(self):

    def collision(self, mousePos, px, py):

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

        if (self.radius+70 > math.sqrt((px - self.x)**2 + (py - self.y)**2)):

            if px > self.x:
                if py > self.y:
                    print("The point is in the top-left quadrant.")
                    self.vx, self.vy = -1, -1
                elif py < self.y:
                    print("The point is in the bottom-left quadrant.")
                    self.vx, self.vy = -1, 1
            elif px < self.x:
                if py > self.y:
                    print("The point is in the top-right quadrant.")
                    self.vx, self.vy = 1, -1
                elif py < self.y:
                    print("The point is in the bottom-right quadrant.")
                    self.vx, self.vy = 1, 1

            #self.vx = -self.vx
            #self.vy = -self.vy
        else:
            self.vx = 0
            self.vy = 0


