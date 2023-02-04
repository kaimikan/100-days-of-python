from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.setx(0)
        self.sety(270)
        self.color("white")
        self.hideturtle()
        self.draw_score()

    def get_high_score(self):
        with open("high_score.txt") as file:
            contents = file.read()
            return int(contents)

    def save_new_high_score(self):
        with open("high_score.txt", mode="w") as file:
            file.write(str(self.high_score))

    def increase_score(self):
        self.score += 1

        if self.score > self.high_score:
            self.high_score = self.score

        self.draw_score()

    def draw_score(self):
        self.clear()
        self.write(f"Apples collected: {self.score}, Most apples ever: {self.high_score}", move=False, align="center",
                   font=('Courier', 18, 'bold'))

    def reset(self):
        if self.high_score > self.get_high_score():
            self.save_new_high_score()
        self.score = 0
        self.draw_score()

    # def game_over(self):
    #     # self.clear()
    #     self.setx(0)
    #     self.sety(0)
    #     self.write(f"GAME OVER", move=False, align="center", font=('Courier', 20, 'bold'))
