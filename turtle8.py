import turtle

screen = turtle.Screen()

k = int(turtle.numinput("Pasul", "Pasul", 10, minval=1, maxval=20))  # pasul
loop = int(turtle.numinput("Numar spirale", "Numar spirale", 10, minval=1, maxval=100))

i = 0
while i <= (loop * 4):
    turtle.forward(k)
    turtle.left(90)
    k += 5
    i += 1

screen.exitonclick()
