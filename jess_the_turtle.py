#!C:/Python27/python.exe

# Created by Jessica Joseph 2015 05 13
import turtle
from time import sleep

def draw_square():
    window = turtle.Screen()
    window.bgcolor("black")
    jess = turtle.Turtle()

    jess.shape("turtle")
    jess.color("orange")
    jess.shapesize(2,0,7)
    jess.pensize(2.5)
    jess.speed(1)

    jess.pensize(1)
    jess.color("red")
    jess.circle(50)
    jess.speed(6)
    jess.circle(100)
    jess.circle(150,180)
    jess.up()
    jess.left(90)
    ##jess.forward(150)
    jess.pendown()
    jess.color("white")
    jess.circle(125,150)
    jess.right(150)
    jess.up()
    jess.forward(200)
    jess.down()
    jess.color("#69BECC")
    jess.pensize(1.5)
    jess.forward(38)
    jess.right(90)
    jess.forward(240)
    #jess.left(30)
    #jess.forward(130)
    #jess.left(235)
    #jess.forward(265)
    jess.color("#69BECC")
    for x in range(4):
        jess.forward(100)
        jess.left(90)
    jess.circle(238)
    #jess.left(12)
    jess.circle(100)
    jess.circle(50)
    jess.color("yellow")
    jess.right(270)
    jess.circle(120,180)
    jess.color("blue")
    jess.right(90)
    jess.dot(20, "blue")


    window.exitonclick()


draw_square()
