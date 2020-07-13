#!/usr/bin/python3

#Import & initialise pygame
import pygame
import time
pygame.init()

#Set some variables
WIDTH = 1200
HEIGHT = 800

#Draw the playing area
screen = pygame.display.set_mode((WIDTH,HEIGHT))

shapeOn = pygame.Color("yellow")
shapeOff = pygame.Color("black")

class Block:
  blockWidth = 20
  blockHeight = 20

  def __init__(self,x,y):
    self.y = y
    self.x = x

  def show(self,colour):
    #First 2 co-ordinates  = Shape position (on screen)
    #Second 2 co-ordinates = Shape Dimensions (size)
    shapeProperties = pygame.Rect((self.x,self.y),(self.blockWidth,self.blockHeight))
    pygame.draw.rect(screen, colour, shapeProperties)

  def update(self):
    self.show(shapeOn)
    #self.y = self.y + 1
    self.y = pygame.mouse.get_pos()[1] 
    self.x = pygame.mouse.get_pos()[0]
    self.show(shapeOn)

#Create a new object of class Block and say where you want it to start off.
mySquare = Block(1,1)

#Show the new object on the screen
mySquare.show(100)


while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    mySquare.update()
    #Force pygame to draw the screen.
    pygame.display.flip()
    
pygame.quit()
