# File for running all turtle code and generating structure
import turtle
from act1_cowabunga import generateCowabunga
from ex_dragon import generateDragon
from ex_fern import generateFern
from ex_arrow import generateArrow
from ex_weave import generateWeave

# initialization
t = turtle.Turtle()
t.shape("turtle")
t.speed(10)
t.left(90)

# This variable determines how far the turtle
# moves everytime we call the goForward function
moveDistance = 10
# The angle at which the turtle runs
turnAmount = 22.5
# Fancy Computer-Sciency data structure that helps us
# keep track of all the coordinates we visit while generating structures with turtle
stack = []


#Enables the turle to go forward by the distance, moveDistance
def goForward():
  t.forward(moveDistance)


# Turns the turtle left by the turn amount
def goLeft():
  t.left(turnAmount)


# Turns the turtle right by the turn amount
def goRight():
  t.right(turnAmount)


# 10 points if you can guess what this does!
def doNothing():
  pass


# Put stuff onto the stack (fancy CS data strucutre)
def pushStack():
  coor = t.position()
  stack.append(coor)
  # print(f"pushed {coor}")


# Get stuff out of the stack (fancy CS data strucutre)
def popStack():
  coor = stack.pop()
  t.penup()
  t.goto(coor)
  t.pendown()
  # print(f"popped {coor}")


# Map stuff from our replacement rules to the functions above
actions = {
  "f": goForward,
  "+": goLeft,
  "-": goRight,
  "x": doNothing,
  "y": doNothing,
  "[": pushStack,
  "]": popStack
}

# Generates the structure  according to the given code
def run(structure):
  for i in structure:
    actions[i]()


# # Run this!
# run(generateCowabunga(5))
# examples
# run(generateDragon(10)) #angle = 90
run(generateFern(5)) #angle = 22.5
# run(generateArrow(7)) #angle = 60
# run(generateWeave(3)) #angle = 90