import turtle
import math

nextDirection = {
  'right': 'down',
  'down': 'left',
  'left': 'up',
  'up': 'right',
}

def main():
  screen = turtle.Screen()
  screen.setup(900, 900)
  t = turtle.Turtle()
  #   penSize = 2
  #   t.pensize(penSize)
  goldenSpiral(t, 1, 1, {'x': 0, 'y':0}, 'right', True)

  turtle.done()

def drawBox(t, length, point = {'x': 0, 'y': 0}):
  move(t, point)
  t.setheading(90)
  for _ in range(4):
    t.forward(length)
    t.right(90)

def goldenSpiral(t, length, lastLength, currentPoint, direction, firstTime):
  if length > 1000:
    return

  drawBox(t, length, currentPoint)

  newPoint = nextPoint(direction, length, lastLength, currentPoint)
  newDirection = nextDirection[direction]

  if firstTime:
    goldenSpiral(t, length, length, newPoint, newDirection, False)
  else:
    goldenSpiral(t, length + lastLength, length, newPoint, newDirection, firstTime)

def nextPoint(dir, length, lastLength, currentPoint):
  point = {'x': currentPoint['x'], 'y': currentPoint['y']}
  if dir == "right":
    point['x'] += length
    if(length != lastLength):
      point['y'] -= lastLength
    
  if dir == "down":
    point['x'] -= lastLength
    point['y'] -= length + lastLength
  if dir == "left":
    point['x'] -= length + lastLength
  if dir == "up":
    point['y'] += length
  return point




def move(t, p = {'x': 0, 'y': 0}):
  t.penup()
  t.goto(p['x'], p['y'])
  t.pendown()



if __name__ == "__main__":
  main()