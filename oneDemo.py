from turtle import *
reset()

iterations = 36
moveDistance = 15
turnAmount = 10

for _ in range(iterations):
    forward(moveDistance)
    left(turnAmount)

exitonclick()
