import turtle
t = turtle.Turtle()
turtle.Screen().bgcolor("black")
t.speed(100)
t.width(2)


t.pencolor("yellow")
for i in range(1,41):
    t.circle(i*5)
t.right(90)
for i in range(1,41):
    t.circle(i*5)
t.right(90)
for i in range(1,41):
    t.circle(i*5)
t.right(90)
for i in range(1,41):
    t.circle(i*5)
t.right(45)    

for i in range(1,41):
    t.circle(i*5)
t.right(90)
for i in range(1,41):
    t.circle(i*5)
t.right(90)
for i in range(1,41):
    t.circle(i*5)
t.right(90)
for i in range(1,41):
    t.circle(i*5)
t.right(135)

t.pencolor("brown")
for i in range(5):
    t.fillcolor("brown")
    t.begin_fill()
    t.circle(i*10)
    t.end_fill()
    t.penup()
    t.setpos(0,-10*i)
    t.pendown()
