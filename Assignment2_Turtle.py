# Assignment 2
# Author: Iskander Kenzhebekov

#import a turtle and random for the color of the roof
import turtle
import random
# Create our turtle
t = turtle.Turtle()
t.getscreen()

# A code to draw the one piece of a fence
def one_fence():
  t.fillcolor("brown")
  t.begin_fill()
  t.forward(100)
  t.left(45)
  t.forward(20)
  t.left(90)
  t.forward(20)
  t.left(45)
  t.forward(100)
  t.left(90)
  t.forward(28.284)
  t.end_fill()

# A code to draw "Special fence" with the handle on it
def special_fence1():
  one_fence()
  t.left(90)
  t.penup()
  t.forward(60)
  t.left(90)
  t.forward(27)
  t.left(90)
  t.pendown()
  t.fillcolor("black")
  t.begin_fill()
  t.circle(11.142)
  t.end_fill()
  t.right(90)
  t.forward(1.284)
  t.left(90)
  t.forward(60)
  t.left(90)
  t.forward(28.284)

# A code to draw a door hinge (fucntion with parameter)
def door_hinge(n):
  count = 0
  while count < n:
    t.fillcolor("grey")
    t.begin_fill()
    t.forward(10)
    t.left(90)
    t.forward(12)
    t.left(90)
    count= count + 1 
    t.end_fill()
  
# A code to draw another "Special fence" but in this time with the door hinge on it
def special_fence2():
  one_fence()
  t.left(180)
  t.forward(28.284)
  t.right(90)
  one_fence()
  t.left(90)
  t.penup()
  t.forward(65)
  t.right(90)
  t.forward(6)
  t.left(90)
  t.pendown()
  door_hinge(2)
  t.penup()
  t.left(180)
  t.forward(50)
  t.left(180)
  t.pendown()
  door_hinge(2)
  t.penup()
  t.left(180)
  t.forward(15)
  t.left(90)
  t.forward(22.284)
  t.pendown()
  
# A code to draw the whole fence 
def whole_fence():
  count=0
  n = 19
  while count < n:
    one_fence()
    t.left(180)
    t.forward(28.284)
    t.right(90)
    count = count + 1
    while count == 9:
      special_fence1()
      t.left(180)
      t.forward(28.284)
      t.right(90)
      count = count + 1
    while count == 11:
      special_fence2()
      t.left(180)
      t.forward(56.568)
      t.right(90)
      count = count + 2

#A code to draw the sky
def sky():
  t.penup()
  t.goto(-270,50)
  t.pendown()
  t.fillcolor("light blue")
  t.begin_fill()
  for i in range(2):
    t.forward(535)
    t.left(90)
    t.forward(215)
    t.left(90)
  t.end_fill()

#A code to draw a house roof 
def house_roof(): 
  t.penup()
  t.goto(80,150)
  t.pendown()
# make the different colors so turtle will chose the random
  colours1 = ["red", "grey", "black"]
  t.fillcolor(random.choice(colours1))
  t.begin_fill()
  t.forward(170)
  t.left(90)
  t.forward(87)
  t.left(90)
  t.forward(222)
  t.left(120)
  t.forward(100)
  t.left(60)
  t.forward(30)
  t.end_fill()
  t.penup()
  t.goto(80,150)
  t.pendown()
  # make the different colors so turtle will chose the random
  colours2 = ["brown", "black", "grey"]
  t.fillcolor(random.choice(colours2))
  t.begin_fill()
  for i in range(3):
    t.left(120)
    t.forward(102)
  t.end_fill()

# A code to draw a house frame.
def house():               
  t.penup()                
  t.goto(-20,150)
  t.pendown()
  t.right(90)
  t.fillcolor("white")
  t.begin_fill()
  for i in range(2):
    t.forward(100)
    t.left(90)
    t.forward(270)
    t.left(90)
  t.end_fill()
  t.penup()                
  t.goto(80,50)
  t.pendown()
  t.left(180)
  t.forward(100)

# A code to draw door and windows of the house
def door_windows():           
  t.penup()                
  t.goto(10,50)
  t.pendown()
  t.fillcolor("brown")
  t.begin_fill()
  for i in range(2):
    t.forward(60)
    t.right(90)
    t.forward(40)
    t.right(90)
  t.end_fill()
  # A code to draw the door knob
  t.penup()            
  t.goto(45,75)
  t.pendown()
  t.fillcolor("black")
  t.begin_fill()
  t.circle(2,360)
  t.end_fill()
  # A code for the window №1
  t.penup()          
  t.goto(105,115)
  t.pendown()
  t.fillcolor("light blue")
  t.begin_fill()
  for i in range(4):
    t.right(90)
    t.forward(30)
  t.end_fill()
  t.penup()                  
  t.goto(120,115)
  t.pendown()
  t.right(180)
  t.forward(30)
  t.right(90)
  t.penup()                  
  t.goto(135,100)
  t.pendown()
  t.forward(30)
  # A code to draw window №2
  t.penup()                 
  t.goto(190,85)
  t.pendown()
  t.fillcolor("light blue")
  t.begin_fill()
  for i in range(4):
    t.right(90)
    t.forward(30)
  t.end_fill()
  t.penup()                  
  t.goto(205,115)
  t.pendown()
  t.left(90)
  t.forward(30)
  t.right(90)
  t.penup()                  
  t.goto(220,100)
  t.pendown()
  t.forward(30)

# A code to draw a garden (with parameter)
def garden(x, y):
  t.right(180)
  t.penup()
  t.goto(-250 + x,-250 + y)
  t.pendown()
  t.fillcolor("green")
  t.begin_fill()
  for i in range(2):
    t.forward(535)
    t.left(90)
    t.forward(310)
    t.left(90)
  t.end_fill()

# A code to draw a sun
def sun():
  t.penup()
  t.goto(-270,200)
  t.pendown()
  t.right(90)
  t.color("yellow")
  t.fillcolor("yellow")
  t.begin_fill()
  t.circle (65,90)
  t.left(90)
  t.goto(-270,265)
  t.left(90)
  t.forward(40)
  t.end_fill()


  

# A code to finally draw everything. 
sky()
house_roof()
house()
door_windows()
garden(-20,-10)
t.penup()
t.goto(265,-220)
t.left(90)
t.pendown()
whole_fence()  
sun()

turtle.done()
