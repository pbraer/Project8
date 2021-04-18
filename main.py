print("""
Project #8 Logo
Разработчик:
Браер П.С.
""")

import turtle
turtle.screensize(600, 600)
turtle.bgcolor('black')
turtle.pencolor('white')
turtle.pensize(2)
turtle.speed(999999)


def background(length, minimum):
    if length < minimum:
        return
    angle = 90
    length = length // 2
    for i in range(2):
        for j in range(2):
            turtle.forward(length)
            turtle.left(angle)
            turtle.forward(length)
            turtle.left(angle)
            background(length, minimum)
            turtle.left(angle)
            turtle.forward(length)
            turtle.right(angle)
            turtle.forward(length)
        angle = -angle


def black_square(side):
    turtle.up()
    turtle.goto(- side / 2, side / 2)
    turtle.pencolor('black')
    turtle.fillcolor('black')
    turtle.down()
    turtle.begin_fill()
    for step in range(4):
        turtle.forward(side)
        turtle.right(90)
    turtle.end_fill()
    turtle.up()
    turtle.home()


def tree(branch):
    if branch > 0:
        turtle.forward(branch)
        turtle.right(20)
        tree(branch - 13)
        turtle.left(40)
        tree(branch - 13)
        turtle.right(20)
        turtle.backward(branch)


def full_tree():
    turtle.left(90)
    turtle.up()
    turtle.backward(100)
    turtle.down()
    turtle.color("red")
    tree(75)


def word():
    turtle.up()
    turtle.down()
    turtle.pencolor('white')
    turtle.write('FREE', align = 'center', font = ('Arial Black', 35, "normal"))
    turtle.up()


screen = turtle.Screen()
background(300, 30)
black_square(300)
full_tree()
word()
screen.exitonclick()

turtle.done()
