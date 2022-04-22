from turtle import *

moveDistance = 120
turnAmount = 60

def goForward(): forward(moveDistance)

def turnLeft(): left(turnAmount)

def turnRight(): right(turnAmount)

actions = {
    "f":goForward,
    "+":turnLeft,
    "-":turnRight
}

def runThis(structure):
    for _ in structure: actions[_]()

reset()

for _ in range(6):
    runThis("f+")

exitonclick()
