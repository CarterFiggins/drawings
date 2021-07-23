import turtle
import random
import time
import math

def main():
  screen = turtle.Screen()
  screen.setup(900, 900)
  drawSpikes()

def drawSpikes():
  t = turtle.Turtle()
  penSize = 2
  t.pensize(penSize)
  t.speed(0)

  x = -350
  y = -350
  length = 3000
  depth = 5
  angle = 45

  for rounds in range(depth+1):
    length = length / 3
    move(t, x, y)
    t.setheading(angle)

    turns = getTurns(rounds)
    for turn in turns:
      t.forward(length)
      if(turn == 'l'):
        t.left(60)
      else:
        t.right(120)

    t.forward(length)
    time.sleep(1)
    if depth != rounds:
      t.clear()

  turtle.done()

def getTurns(depth):
  if(depth == 0):
    return[]

  if(depth == 1):
    return ['l', 'r', 'l']

  return getTurns(depth - 1) + ['l'] + getTurns(depth - 1) + ['r'] + getTurns(depth - 1) + ['l'] + getTurns(depth - 1)

def move(t, x, y):
  t.penup()
  t.goto(x,y)
  t.pendown()

if __name__ == "__main__":
    main()