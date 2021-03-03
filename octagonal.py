# Dibuja un octagono con una espiral dentro

from turtle import *

def octagon(tortuga, x, y, color):
    tortuga.pencolor(color)
    tortuga.penup()
    tortuga.setposition(x, y)
    tortuga.pendown()
    for i in range(8):
        tortuga.forward(80)
        tortuga.right(45) 

def spiral(tortuga, x, y, color):
    distance = 0.2
    angle = 40
    tortuga.pencolor(color)
    tortuga.penup()
    tortuga.setposition(x, y)
    tortuga.pendown()
    for i in range(130):
        tortuga.forward(distance)
        tortuga.left(angle)
        distance += 0.5   
        
tortuga = Turtle()
octagon(tortuga, -45, 100, 'red')
spiral(tortuga, 0, 0, 'blue')
tortuga.hideturtle()
done()