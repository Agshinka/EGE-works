from turtle import *
left(90)
size =30
screensize(1500, 1500)
tracer(0)
down()
right(45)
for i in range (3):
    forward(5 * size)
    right(45)
    forward(10 * size)
    right(135)
up()
for x in range (-50, 50):
    for y in range (-50, 50):
        setpos(x * size, y * size)
        dot(4, 'red')
done()