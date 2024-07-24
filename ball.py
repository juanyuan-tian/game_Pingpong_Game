from turtle import Turtle
import math
class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.fillcolor("white")
        self.penup()
        # self.setheading(math.degrees(math.atan(3 / 4))) 我直接用三角函数
        # 这么精确
        self.x_move = 10  # movement pixel
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # new_x = self.xcor() + 10
        # new_y = self.ycor() - 10  y坐标变化，方法搞复杂了！
        # self.goto(new_x, new_y)
        self.y_move *= -1

    def bounce_x(self):
        # new_x = self.xcor() + 10
        # new_y = self.ycor() - 10  y坐标变化，方法搞复杂了！
        # self.goto(new_x, new_y)

        # increase speed  不是用turtle 做，用time.sleep做
        # self.x_move = 20
        self.x_move *= -1
        self.move_speed *= 0.9


