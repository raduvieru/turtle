import math
import turtle

num_linii = turtle.numinput("Numar raze", "Numar raze", 15, minval=1, maxval=100)
raza = turtle.numinput("Lungimea razei", "Lungimea razei", 100, minval=10, maxval=900)

angle = 0
while angle < 360:
    turtle.goto(raza * math.cos(angle * math.pi / 180), raza * math.sin(angle * math.pi / 180))
    turtle.goto(0,0)
    angle = angle + (360/num_linii)

turtle.mainloop()
#exitonclick()
