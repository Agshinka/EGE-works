from turtle import *
m = Turtle()
m.reset()
m.left(90)
size = 30
screensize(3000, 3000)
tracer(0)
m.down()
m.right(180)
m.forward(2 * size)
m.right(90)
m.forward(40 * size)
m.right(90)
m.forward(2 * size)
for i in range (4):
    m.seth(90)
    m.circle(-5 * size,180)
m.up()
for x in range (-50, 50):
    for y in range (-50, 50):
        m.setpos(x * size, y * size)
        m.dot(4, 'red')
done()