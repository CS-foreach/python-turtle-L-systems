from turtle import *

def drawThis(iterations, moveDistance, turnAmount):
    for _ in range(iterations):
        forward(moveDistance)
        left(turnAmount)

reset()

drawThis(10, 11, 18)
left(180)
drawThis(10, 15, -22)

exitonclick()
