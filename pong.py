#!/usr/bin/python3

#import what we need
import pygame
import os

#Initalise Pygame
pygame.init()

#Set some variables
WIDTH = 1200
HEIGHT = 800
BORDER = 20
VELOCITY = 10

#Draw the playing area
screen = pygame.display.set_mode((WIDTH,HEIGHT))
fgcolour = pygame.Color("white")
bgcolour = pygame.Color("black")

#Define Classes
class Ball:
    RADIUS = 20
    def __init__(self,x,y,vx,vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def show(self, colour):
        #global screen
        pygame.draw.circle(screen, colour, (self.x, self.y), self.RADIUS)
    
    def update(self):
        #global bgcolour, fgcolour
        self.show(bgcolour)
        if self.x == 40:
            self.vx = self.vx * -1

        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(fgcolour)
        

class Paddle:
    pass

#Create Objects
ballplay = Ball(WIDTH-Ball.RADIUS, HEIGHT//2, -VELOCITY,0)

#Draw the border which is made up of 3 rectangles
##Define each rectangle which will be drawn to make up the border
rect1 = pygame.Rect((0,0),(WIDTH,BORDER))
rect2 = pygame.Rect((0,780),(WIDTH,BORDER))
rect3 = pygame.Rect((0,0),(BORDER,HEIGHT))
##Actually draw each rectangle to make the border
pygame.draw.rect(screen, fgcolour, rect1)
pygame.draw.rect(screen, fgcolour, rect2)
pygame.draw.rect(screen, fgcolour, rect3)

#Show the ball object
ballplay.show(fgcolour)

#Everything actually takes place within this loop, including the exit event which is handled by pygame.QUIT
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    ballplay.update()
    #Force pygame to draw the screen.
    pygame.display.flip()
pygame.quit()

