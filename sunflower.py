import math
import turtle

#inicial
turtle.bgcolor("black")
turtle.shape("turtle")
turtle.speed(0)
turtle.fillcolor("brown")

# tallo
turtle.penup()
turtle.goto(0, -300)
turtle.pendown()
turtle.setheading(90)
turtle.fillcolor("green")  
turtle.begin_fill()
turtle.forward(200)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(200)
turtle.end_fill()

# centro del girasol
turtle.penup()
turtle.goto(0, -180)
turtle.fillcolor("#8B4513")  
turtle.begin_fill()
turtle.circle(0)
turtle.end_fill()

# pétalos del girasol
phi = 137.508 * (math.pi / 180.0)
for i in range(160 + 40):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(i * 137.508)
    turtle.pendown()
    if i < 160:
        turtle.stamp()
    else:
        turtle.fillcolor("yellow")
        turtle.begin_fill()
        turtle.right(20)
        turtle.forward(70)
        turtle.left(40)
        turtle.forward(70)
        turtle.left(140)
        turtle.forward(70)
        turtle.left(40)
        turtle.forward(70)
        turtle.end_fill()

# Oculta el cursor 
turtle.hideturtle()

# Cierra la ventana
turtle.exitonclick()