from random import choice, randint
from turtle import Turtle, Screen


timmy = Turtle()
timmy.speed('fastest')


def random_color():
    r = randint(0, 255)/ 255.0
    g = randint(0, 255)/ 255.0
    b = randint(0, 255)/ 255.0
    random_color = (r, g, b)
    return random_color

for i in range(1, 1000, 10):
    timmy.color(random_color())
    timmy.circle(150)
    timmy.setheading(i)


        
screen = Screen()
screen.exitonclick()