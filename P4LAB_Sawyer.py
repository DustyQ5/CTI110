# It draws a four pointed star using a square and four tirangles
# 10/9/2018
# CTI-110 
# Chazz Sawyer
#



import turtle

wn = turtle.Screen()

bit = turtle.Turtle()
bit.color("red")
bit.pensize(3)
for square in [0,1,2,3]:
    bit.forward(60)
    bit.right(90)
    for triangle in[0,1,2]:
        bit.forward(60)
        bit.left(120)
       



