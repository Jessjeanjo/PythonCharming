#!C:/Python27/python.exe

import turtle
from time import sleep

def draw_square(turtle):
    for i in range(4):
        turtle.fd(100)
        turtle.right(90)

def draw_squareCircle():
    window = turtle.Screen()
    window.bgcolor("black")
    jess = turtle.Turtle()

    jess.shape("turtle")
    jess.color("orange")
    jess.shapesize(2,0,7)
    jess.pensize(2.5)
    jess.speed(6)
    for i in range(37):
        draw_square(jess)
        jess.right(10)

    window.exitonclick()


draw_squareCircle()
