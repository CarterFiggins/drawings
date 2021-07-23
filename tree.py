import turtle
import random

def main():
  screen = turtle.Screen()
  screen.setup(1000, 900)
  t = turtle.Turtle()
  x = 10
  y = -400
  penSize = 25
  t.pensize(penSize)
  t.speed(0)
  t.color('#8a2027')
  move(t, x, y)
  tree(t, 0, 90, 180, penSize)
  turtle.done()

def tree (t, depth, deg, f, size):
  t.pensize(size)
  if depth == 6:
    return
  
  t.color('#8a2027')
  t.setheading(deg)
  t.forward(f)
  pos = t.pos()
  tree(t, depth+1, deg+random.randint(30, 40), f-25, size-4.1)
  move(t, pos[0], pos[1])
  tree(t, depth+1, deg-random.randint(30, 40), f-25, size-4.1)

  if depth >= 3:
    move(t, pos[0], pos[1])
    tree(t, depth+1, deg+random.randint(0,25), f-25, size-4.1)
    move(t, pos[0], pos[1])
    tree(t, depth+1, deg-random.randint(0,25), f-25, size-4.1)

  if depth == 5:
    leaf(t)
    
def leaf (t):
  turtle.colormode(255) 
  color = (254, random.randint(100,190), random.randint(150, 190))
  t.pencolor(color)
  t.fillcolor(color)
  for _ in range(5):
    t.begin_fill()
    t.circle(45,70)
    t.left(110)
    t.circle(45,70)
    t.end_fill()

def move(t, x, y):
  t.penup()
  t.goto(x,y)
  t.pendown()

if __name__ == "__main__":
    main()