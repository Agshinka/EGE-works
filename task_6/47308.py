from turtle import *
left(90)
size = 30
screensize(1500, 1500)
tracer(0)
down()
for i in range (5):
    forward(8 * size)
    right(60)
    forward(8 * size)
    right(120)
up()
for x in range (-50, 50):
    for y in range (-50, 50):
        setpos(x * size, y * size)
        dot(4, 'red')
done()