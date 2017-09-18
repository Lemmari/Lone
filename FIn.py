#Allow player to move
#Randomly generate enemies at random points of the grid
#Randomly generate weapons for said enemies
#Allow turn-based attacks for player and enemy
#Allow player to attack
#Allow player to get items from enemies

import time
import random

x = 0
y = 0
Grid = (x, y)
hp = 40

def Movement():
  global Grid
  global x
  global y
  
  Move = input("> ")
  Move = Move.lower()
  
  #print(Move)
  
  if Move == 'foward' or Move == 'f':
    y = y+1
  elif Move == 'back' or Move == 'b':
    y = y-1
  elif Move == 'right' or Move == 'r':
    x = x+1
  elif Move == 'left' or Move == 'l':
    x = x-1
  
  Grid = (x, y)
  return x, y, Grid

while hp > 0:
  Movement();
  print(Grid)
  #print(x)
  #print(y)
