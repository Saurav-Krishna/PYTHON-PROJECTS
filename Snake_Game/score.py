from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("red")
        self.clear()
        self.penup()
        self.goto(0,260)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f'Score : {self.score}', align=ALIGNMENT, font=FONT)
        with open("high score.txt", 'w' ) as file
            file.write(str(self.score))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over" , align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def high_score(self):

        with open("high score.txt") as file:
            high_score= file.read()
        self.write(f'High Score : {high_score}', align=ALIGNMENT, font=FONT)

        if self.score <= int(high_score):
            high_score

        else:
            self.score = high_score
