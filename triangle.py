import turtle
import math

def main():
  t = turtle.Turtle()
  penSize = 2
  t.pensize(penSize)
  t.speed(0)
  length = 900
  height = (length/2) * math.sqrt(3)
  x = -(length/2)
  y = -(height/2)

  leftPoint = { 'x': x, 'y': y }
  topPoint = { 'x': x + (length / 2), 'y': y + height }
  rightPoint = { 'x': x + length, 'y': y }

  drawTriangle(t, topPoint, rightPoint, leftPoint)
  t.fillcolor('white')
  sierpinskiTriangle(t, topPoint, rightPoint, leftPoint, 0)

  turtle.done()

def drawTriangle(t, p1, p2, p3):
  move(t, p3['x'], p3['y'])
  t.begin_fill()
  t.goto(p1['x'], p1['y'])
  t.goto(p2['x'], p2['y'])
  t.goto(p3['x'], p3['y'])
  t.end_fill()

def sierpinskiTriangle(t, topPoint, rightPoint, leftPoint, depth):
  if depth == 6:
    return

  midPointTR = midpointFormula(topPoint, rightPoint)
  midPointRL = midpointFormula(rightPoint, leftPoint)
  midPointLT = midpointFormula(leftPoint, topPoint)

  drawTriangle(t, midPointTR, midPointRL, midPointLT)

  sierpinskiTriangle(t, topPoint, midPointTR, midPointLT, depth + 1)
  sierpinskiTriangle(t, midPointTR, rightPoint, midPointRL, depth + 1)
  sierpinskiTriangle(t, midPointLT, midPointRL, leftPoint, depth + 1)
  
def midpointFormula(p1, p2):
  return{
    'x': (p1['x'] + p2['x'])/2,
    'y': (p1['y'] + p2['y'])/2,
  } 

def move(t, x, y):
  t.penup()
  t.goto(x,y)
  t.pendown()

if __name__ == "__main__":
    main()