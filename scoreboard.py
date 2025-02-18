from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(8, 250)
        self.score = 0
        try:
            with open("data.txt") as data:
                self.high_score = int(data.read())
        except FileNotFoundError:
            self.high_score = 0
            with open("data.txt", mode="w") as data:
                data.write("0")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(
            arg=f"Score:{self.score} High Score:{self.high_score}",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
