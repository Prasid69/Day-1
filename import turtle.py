import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
s.bgcolor("black")
t.pencolor("cyan")
a=0
b=0
t.speed(0)
t.penup()
t.goto(-10,230)
t.pendown()
while True:
    t.forward(a)
    t.right(b)
    a+=4
    b+=1
    if b==300:
        break
    t.hideturtle()
    turtle.done