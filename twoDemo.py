from turtle import *
reset()

def drawThis(iterations, moveDistance, turnAmount):
    for _ in range(iterations):
        forward(moveDistance)
        left(turnAmount)

drawThis(10, 11, 18)
left(180)
drawThis(10, 15, -22)

exitonclick()
