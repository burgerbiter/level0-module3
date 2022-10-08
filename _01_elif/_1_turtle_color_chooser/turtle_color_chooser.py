import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    for i in range(10):
        tot = turtle.Turtle()
        tot.speed(0)
        tot.circle(100,360,4)
        tot.pensize(10)
        color = simpledialog.askstring(title="Color",prompt="What color would you like to draw with?")
        if color == ("green"):
            tot.pencolor('green')
        elif color == ("red"):
            tot.pencolor('red')
        elif color == ("blue"):
            tot.pencolor('blue')
        else:
            tot.pencolor(color.random)


    # TODO 1) Create a new Turtle
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    #      3) Set the pen width to 10
    #      4) Ask the user what color pen they would like to draw with
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
