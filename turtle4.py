import turtle
import math

turtle.penup()

angle = 0

radius = turtle.numinput("Raza" , "Introduceti Raza", 100 , minval=5 , maxval=1000)
xpoz = turtle.numinput("X-Poz" , "Introduceti coordonata X", 0 , minval=0 , maxval=1000)
ypoz = turtle.numinput("Y-Poz" , "Introduceti coordonata Y", 0 , minval=0 , maxval=1000)

turtle.pen(fillcolor="black", pencolor="red", pensize=10)

turtle.goto((radius * math.cos(angle*math.pi/180) + xpoz), (radius * math.sin(angle*math.pi/180) + ypoz))
turtle.pendown()
angle += 1
while angle <= 360:
    turtle.goto((radius * math.cos(angle*math.pi/180) + xpoz), (radius * math.sin(angle*math.pi/180) + ypoz))
    angle += 1

turtle.mainloop()
