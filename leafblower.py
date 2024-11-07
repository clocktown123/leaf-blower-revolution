import pygame
from pygame.math import Vector2
A = 0
D = 1
W = 2
S = 3


class player:
    def __init__ (self):
        self.pos = Vector2(200,615)
        self.vx=0
        self.vy=0
        self.direction = D
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255,0,255), (self.pos.x, self.pos.y, 50, 50))
    
    def move(self, keys):
        if keys[A] == True:
            self.vx = -3
            self.direction = A
        elif keys[D] == True:
            self.vx = 3
            self.direction = D
        else:
            self.vx = 0

        if keys[W] == True:
            self.vy = -3
            self.direction = W
        elif keys[S] == True:
            self.vy = 3
            self.direction = S
        else:
            self.vy = 0
        
        self.pos.y += self.vy
        self.pos.x += self.vx
