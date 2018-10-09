# Turtles draw a square and a triangle
# 10/9/2018
# CTI-110 P4T1a: Shapes
# Chazz Sawyer
#

import turtle

wn = turtle.Screen()
wn.bgcolor("pink")
wn.title("Bit and Blip")

bit = turtle.Turtle()
bit.color("red")
bit.pensize(10)
for M in [0,1,2,3]:
    bit.forward(60)
    bit.right(90)
    
blip = turtle.Turtle()
blip.color("green")
blip.pensize(7)
for N in [0,1,2]:
    blip.forward(100)
    blip.left(120)

    






