import turtle
from math import pi, sin

screen = turtle.Screen()

def poligon(n, r):
    if n < 3:
        exit()
    turtle.penup()
    alpha = (n - 2) * 180 / n #marimea ungiului intern din poligon
    #turtle.reset()
    turtle.goto(0, 0)
    turtle.forward(r)
    turtle.left(180 - alpha/2)
    # turtle.left(-alpha / 2)
    turtle.pendown()
    i = 0
    while i < n:
        turtle.forward(2 * r * sin(pi / n))
        turtle.left(180 - alpha)
        i += 1

plg_num = int(turtle.numinput("Numar poligoane", "Numar poligoane", 3, minval=3, maxval=20))
raza = int(turtle.numinput("Numar poligoane", "Numar poligoane", 40, minval=3, maxval=100))
j = 3
while j <= plg_num+3:
    poligon(j, raza)
    raza += 20
   # plg_num += 1
    j += 1

screen.exitonclick()
