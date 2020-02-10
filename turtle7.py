import turtle
from math import pi, sin, cos

screen = turtle.Screen()

k = turtle.numinput("Pasul", "Pasul", 10, minval=1, maxval=20)  # pasul
i = 0
while i <= 200:
    alpha = i / 20 * pi
    x = k * alpha * cos(alpha)
    y = k * alpha * sin(alpha)
    turtle.goto(x, y)
    i += 1
screen.exitonclick()
