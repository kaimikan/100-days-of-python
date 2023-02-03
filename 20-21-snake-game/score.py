from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.setx(0)
        self.sety(270)
        self.color("white")
        self.hideturtle()
        self.draw_score()

    def increase_score(self):
        self.score += 1
        self.draw_score()

    def draw_score(self):
        self.clear()
        self.write(f"Apples collected: {self.score}", move=False, align="center", font=('Courier', 18, 'bold'))

    def game_over(self):
        # self.clear()
        self.setx(0)
        self.sety(0)
        self.write(f"GAME OVER", move=False, align="center", font=('Courier', 20, 'bold'))
