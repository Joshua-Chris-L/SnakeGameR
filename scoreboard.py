from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score =  0
        self.color("white")
        self.penup()
        with open("my_file.txt", mode="r") as file:
            contents = file.read()
        self.high_score = int(contents)
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High_Score: {self.high_score}", align=ALIGNMENT , font= FONT )
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("my_file.txt", mode="w") as file:
                file.write(self.high_score)
        self.score = 0
        
    def increase_score(self):
        self.score += 1 
        self.update_scoreboard()
        
    """ 
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT , font= FONT )
    """