#!/usr/bin/python3

#Import & initialise pygame
import pygame
import time
import sys 

pygame.init()

#Window Title
pygame.display.set_caption('The worst incarnation of pong that you\'ve ever seen!') 
print()
print("Your score is: ", end='')

#Set some variables
WIDTH = 1000    
HEIGHT = 600
BORDER = 20
VELOCITY = 10
SCORE = 0 

#Draw the playing area
screen = pygame.display.set_mode((WIDTH,HEIGHT))

shapeOn = pygame.Color("white")
shapeOff = pygame.Color("black")

#Define Classes
class Ball:
    RADIUS = 10
    def __init__(self,x,y,vx,vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def show(self, colour):
        pygame.draw.circle(screen, colour, (self.x, self.y), self.RADIUS)
    
    def update(self):
        #global bgcolour, fgcolour
        self.show(shapeOff)
        if self.x == 40:
            self.vx = self.vx * -1
        if self.y == 40:
            self.vy = self.vy * -1
        if self.y == 760:
            self.vy = self.vy * -1
        if self.x == 1200:
            print("Game Over!")

        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(shapeOn)

class Paddle:
  blockWidth = 20
  blockHeight = 100
  score = 0 

  def __init__(self,x,y):
    self.y = y
    self.x = x
    self.score = 1

  def show(self,colour):
    #First 2 co-ordinates  = Shape position (on screen)
    #Second 2 co-ordinates = Shape Dimensions (size)
    shapeProperties = pygame.Rect((self.x,self.y),(self.blockWidth,self.blockHeight))
    pygame.draw.rect(screen, colour, shapeProperties)

  def update(self):
    self.show(shapeOff)
    self.y = pygame.mouse.get_pos()[1] 
    self.show(shapeOn)
 
    

    is_hit = gameBall.y in range(self.y, self.y+100)
    if is_hit == True: 
      if gameBall.x == self.x:
        gameBall.vy = gameBall.vy * -1
        gameBall.vx = gameBall.vx * -1
        print(self.score)
        #sys.stdout.write(str(self.score))
        self.score += 1
        #sys.stdout.flush() 

#Create a new object of class Block and say where you want it to start off.
gamePaddle = Paddle(1140,20)

#Create a new object of class Ball and define its attributes.
gameBall = Ball(WIDTH-Ball.RADIUS, HEIGHT//2, -VELOCITY, -VELOCITY)

#Draw the border which is made up of 3 rectangles
##Define each rectangle which will be drawn to make up the border
rect1 = pygame.Rect((0,0),(WIDTH-60,BORDER))
rect2 = pygame.Rect((0,780),(WIDTH-60,BORDER))
rect3 = pygame.Rect((0,0),(BORDER,HEIGHT))
##Actually draw each rectangle to make the border
pygame.draw.rect(screen, shapeOn, rect1)
pygame.draw.rect(screen, shapeOn, rect2)
pygame.draw.rect(screen, shapeOn, rect3)

#Show the new object on the screen
gamePaddle.show(shapeOn)
gameBall.show(shapeOn)

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    gamePaddle.update()
    gameBall.update()
    
    #Force pygame to draw the screen.
    pygame.display.flip()
    
pygame.quit()
