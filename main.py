from turtle import Turtle,Screen

timmy = Turtle()

def shapes(angle,len):
    timmy.forward(len)
    timmy.right(angle)
def solution(amount):
    # Create list of each shape
    shapes_list = list(range(3,amount))
    for number_rib in shapes_list:
        angle = 360 / number_rib
        print(angle)
        for draw in range(number_rib):
            shapes(angle, 200)
solution(11)





























screen = Screen()
screen.exitonclick()