from turtle import Turtle


class Score(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.accidents = 0
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-self.screen_width / 2 + 25, self.screen_height / 2 - 45)
        self.write(f"Level: {self.level}", align="left", font=("Courier", 25, "normal"))
        self.goto(-self.screen_width / 2 + 25, self.screen_height / 2 - 75)
        self.write(f"Crashes: {self.accidents}", align="left", font=("Courier", 15, "normal"))

    def next_level(self):
        self.level += 1
        self.update_scoreboard()

    def reset_level(self):
        self.level = 1
        self.accidents += 1
        self.update_scoreboard()
