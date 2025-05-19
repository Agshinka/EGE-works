from turtle import *
left(90)
size = 30
screensize(2000, 2000)
tracer(0)
down()
for i in range (9):
    forward(18 * size)
    right(72)
up()
for x in range (-50, 50):
    for y in range (-50, 50):
        setpos(x * size, y * size)
        dot(4, 'red')
done()