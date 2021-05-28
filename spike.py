import turtle
import random
import math

def main():
  t = turtle.Turtle()
  x = 0
  y = 0
  penSize = 2
  t.pensize(penSize)
  t.speed(0)

  pt1 = {'x': -600, 'y': -400}
  pt2 = {'x': 1000, 'y': 1000}
  depth = 6
  angle = 45
  length = lengthOfLine(pt1, pt2) / 4**depth
  print(length)

  turns = getTurns(depth)

  move(t, pt1['x'], pt1['y'])
  t.setheading(angle)

  for turn in turns:
    t.forward(length)
    if(turn == 'l'):
      t.left(45)
    else:
      t.right(90)

  t.forward(length)


  turtle.done()

def getTurns(depth):

  if(depth == 0):
    return[]

  if(depth == 1):
    return ['l', 'r', 'l']

  return getTurns(depth - 1) + ['l'] + getTurns(depth - 1) + ['r'] + getTurns(depth - 1) + ['l'] + getTurns(depth - 1)


def midpointFormula(p1, p2):
  return{
    'x': (p1['x'] + p2['x'])/2,
    'y': (p1['y'] + p2['y'])/2,
  } 

def lengthOfLine(p1, p2):
  return math.sqrt((p2['x']- p1['x'])**2 + (p2['y'] - p1['y'])**2)

def move(t, x, y):
  t.penup()
  t.goto(x,y)
  t.pendown()

if __name__ == "__main__":
    main()