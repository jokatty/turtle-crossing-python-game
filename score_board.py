from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.coordinates = coordinates
        self.level = 1
        self.hideturtle()
        self.generate_board()

    def generate_board(self):
        self.penup()
        self.goto(self.coordinates)
        self.color('black')

    def display_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align='left', font=("Courier", 20, "normal"))

    def update_level(self):
        self.level += 1
        self.display_level()

    def game_over(self):
        self.write("GAME OVER", align="center", font=("Courier", 20, "normal"))




