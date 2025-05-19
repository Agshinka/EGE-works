from turtle import *
left(90)
s = 30
screensize(3000, 3000)
tracer(0)
down()
for i in range (5):
    seth(0)
    circle(5 * s, 180)
    seth(90)
    circle(5 * s, 180)
    seth(180)
    circle(5 * s, 180)
    seth(270)
    circle(5 * s, 180)
up()
for x in range (-50, 50):
    for y in range (-50, 50):
        setpos(x * s, y * s)
        dot(4, 'red')
done()