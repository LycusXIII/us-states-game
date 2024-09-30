from turtle import Turtle

FONT = ("Courier", 7, "bold")

class Display(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def show_state(self, state, position):
        self.goto(position)
        self.write(state, align="center", font=FONT)