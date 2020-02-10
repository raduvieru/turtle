import turtle

num_patrate = int(turtle.numinput("Numar Patrate", "Numar Patrate", 5, minval=1, maxval=100))

startx = turtle.numinput('StartX', 'Coordonata X', 0)
starty = turtle.numinput('StartY', 'Coordonata Y', 0)

lat_init = turtle.numinput('Start dimensiune', 'Introduceti dimensiunea initiala patrat:', 100, minval=1, maxval=1000)
step = turtle.numinput('Spatiu Patrat', 'Introduceti spatiul dintre patrate:', 20, minval=1, maxval=100)

for i in range(num_patrate):
    turtle.penup()
    turtle.setx(startx)
    turtle.sety(starty)
    lat = lat_init + step * i * 2
    rad = ((lat ** 2) / 2) ** 0.5
    turtle.right(135)
    turtle.forward(rad)
    turtle.left(135)
    turtle.pendown()
    for j in range(4):
        turtle.forward(lat_init + (step * 2 * i))
        turtle.left(90)

turtle.mainloop()
