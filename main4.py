import colorgram
from turtle import Turtle, Screen
import random
colors = colorgram.extract("image.jpg", 9)
list_colors = []
for c in colors:
    r = c.rgb.r
    g = c.rgb.g
    b = c.rgb.b
    list_colors.append((r, g, b))
print(list_colors)
screen = Screen()
screen.colormode(255)
s = Turtle()


def draw_dots( dots_amount, dot_a_line,dot_size = 10, gaps=50):
    s.setheading(225)
    s.penup()
    s.forward(300)
    s.setheading(0)
    number_of_dots = dots_amount
    dot_in_line = dot_a_line
    for nums in range(1, number_of_dots + 1):
        s.pendown()
        s.dot(dot_size, random.choice(list_colors))
        s.penup()
        s.forward(gaps)
        if nums % dot_in_line == 0:
            s.setheading(90)
            s.forward(gaps)
            s.setheading(180)
            s.forward(gaps * dot_in_line)
            s.setheading(0)

draw_dots(99,7,25,30)
screen.exitonclick()
