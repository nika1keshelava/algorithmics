from turtle import *

my_turtle = Turtle()
my_turtle.speed(20)
my_turtle.color("red")
my_turtle.width(10)
my_turtle.shape("turtle")


for i in range(4):
    my_turtle.forward(100)
    my_turtle.left(90)

for i in range(4):
    my_turtle.forward(200)
    my_turtle.left(90)

for i in range(4):
    my_turtle.forward(300)
    my_turtle.left(90)

my_turtle.left(45)
my_turtle.forward(450)

exitonclick()