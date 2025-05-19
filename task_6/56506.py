from turtle import *
left(90)
size =30
screensize(1500, 1500)
tracer(0)
down()
for i in range (3):
    forward(7 * size)
    right(90)
forward(10*size)
for i in range (3):
    left(90)
    forward(6 * size)
up()
for x in range (-50, 50):
    for y in range (-50, 50):
        setpos(x * size, y * size)
        dot(4, 'red')
done()