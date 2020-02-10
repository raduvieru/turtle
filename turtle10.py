import turtle
from math import pi, sin, cos

screen = turtle.Screen()
screen.delay()

raza = int(turtle.numinput("Raza", "Introduceti Raza", 20, minval=3, maxval=100))
num = int(turtle.numinput("Numar", "Numar de Cercuri", 6, minval=2, maxval=30))

def cerc (raza, a, b): # raza - raza cercului, a,b - coordonatele initiale
    turtle.penup()
    i=0
    turtle.goto(a + raza * cos(i * pi / 180), b + raza * sin(i * pi / 180))
    turtle.pendown()
    while i<= 360:
        turtle.goto(a + raza * cos(i*pi/180), b + raza * sin(i*pi/180))
        i +=1

angle = 360 //num
j=0
while j < 360:
    xpoz = raza * cos(raza + j * pi / 180)
    ypoz = raza * sin(raza + j * pi / 180)
    cerc(40, xpoz, ypoz)
    j+=angle

screen.exitonclick()
