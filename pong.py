#!/usr/bin/python2.7

#import what we need
import pygame
import os
from sys import exit

#Initalise Pygame
pygame.init()

#Set some variables
WIDTH=1200
HEIGHT=800
BORDER=20

#Draw the playing area
screen = pygame.display.set_mode((WIDTH,HEIGHT))
fgcolour = pygame.Color("white")

#Draw the border which is made up of 4 rectangles

##Define each rectangle which will be drawn to make up the border
rect1 = pygame.Rect((0,0),(WIDTH,BORDER))
rect2 = pygame.Rect((0,780),(WIDTH,BORDER))
rect3 = pygame.Rect((0,0),(BORDER,HEIGHT))
rect4 = pygame.Rect((1180,0),(BORDER,HEIGHT))

##Actually draw each rectangle to make the border
pygame.draw.rect(screen, fgcolour, rect1)
pygame.draw.rect(screen, fgcolour, rect2)
pygame.draw.rect(screen, fgcolour, rect3)
pygame.draw.rect(screen, fgcolour, rect4)


#Force pygame to draw the screen.
pygame.display.flip()


#Capture the event when a user closes the window and exit the program
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

pygame.display.quit()

#Yes, this is a horrible hack but I can't get the program to quit without it.
killcmd = "ps -ef | grep -i pong.py | grep -v grep | awk {'print $2'} | xargs kill -9"
os.system(killcmd)