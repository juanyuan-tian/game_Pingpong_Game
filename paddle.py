from turtle import Turtle


class Paddle(Turtle): # 如果我不用单独的refresh函数。 class（） 里面是否可以直接加入变量varible？
    # class里面不加，但是init里面可以加入

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        # self.xposition = 0
        # self.refesh(self.xposition)
    #     但是加了函数，又必须设置一个attribute  self.xposition有了一个初始值
    # 直接删除 是可行的
    #     pass

    # def refesh(self, xposition):
    #
    #     # 这里不需要再建立一个paddle object了，因为已经在Paddle Turtle里面，直接用self.就行
    #     paddle = Turtle()
    #     paddle.shape("square")
    #     paddle.color("white")
    #     paddle.shapesize(stretch_wid=5, stretch_len=1)
    #     paddle.penup()
    #     paddle.goto(x=xposition,y=0)
    #

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)
        # screen.update()

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)
        # x=self.xcor()是个值，不是一个funct作为另一个funct的argument
        # screen.update()








