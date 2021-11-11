from turtle import Turtle,Screen
import random
timmy = Turtle()
timmy.pensize(10)
def random_walk(times):
    angles = [0,90,180,360]
    colors = ["AntiqueWhite1","red","green","brown","yellow","black"]
    timmy.speed(10)
    for time in range(times):
        random_dirc = random.choice(angles)
        timmy.color(random.choice(colors))
        timmy.right(random_dirc)
        timmy.forward(50)
random_walk(100)























screen = Screen()
screen.exitonclick()