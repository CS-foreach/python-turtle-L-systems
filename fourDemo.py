from turtle import *
from dragonGeneration import generateDragon
reset()

moveDistance = 5
turnAmount = 90

def goForward():
    forward(moveDistance)

def turnLeft(): 
    left(turnAmount)

def turnRight(): 
    right(turnAmount)

def doNothing():
    pass

actions = {
    "f":goForward,
    "+":turnLeft,
    "-":turnRight,
    "x":doNothing,
    "y":doNothing
}

def runThis(structure):
    for _ in structure: 
        actions[_]()

tracer(0)
runThis(generateDragon(12))
update()

exitonclick()
