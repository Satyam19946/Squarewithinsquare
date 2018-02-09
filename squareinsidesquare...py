import turtle
import math

t = turtle.Turtle()
wn = turtle.Screen()

side = int(input("Enter the value of the  side of the biggest square>>"))
os = side
ux = side/2
lx = -ux
ly = lx
uy = ux
wn.setworldcoordinates(lx,ly,ux,uy)
t.penup()

def makeasquare(n):
  t.forward(n)
  t.left(90)
  t.forward(n)
  t.left(90)
  t.forward(n)
  t.left(90)
  t.forward(n)
  t.left(90)

def reachpoint(x,y):
  t.penup()
  t.goto(x,y)
  t.pendown()
  
def midpoint(side):
  t.forward(side/2)
  t.left(45)

reachpoint(lx,lx)  
while side>0.5:
  makeasquare(side)
  midpoint(side)
  side = side/math.sqrt(2)  #the side of the new square will be equal to a/root(2) where a is the side of the previous square
  
reachpoint(lx,lx)

print("The Area of sum of all the squares after repeating the process of making \n the squares an infinite amount of times is:")
print(\t(os**2)*(math.sqrt(2)+1))
wn.exitonclick()
