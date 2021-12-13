from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.top_wall = 300
        self.bottom_wall = -300
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def ball_bounce_y(self):
        # change direction
        self.y_move *= - 1

    def ball_bounce_x(self):
        self.x_move *= - 1
        self.ball_speed *= 0.9

    def return_position(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.ball_bounce_x()
