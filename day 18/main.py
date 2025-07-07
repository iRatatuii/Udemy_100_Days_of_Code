from random import choice, randint
from turtle import Turtle, Screen


timmy = Turtle()
timmy.speed('fastest')
timmy.pensize(10)


def random_color():
    r = randint(0, 255)/ 255.0
    g = randint(0, 255)/ 255.0
    b = randint(0, 255)/ 255.0
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
for i in range(200):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(choice(directions))
        
screen = Screen()
screen.exitonclick()