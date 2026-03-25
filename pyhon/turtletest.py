import turtle 

class MyTurtle(turtle.Turtle):
    def __init__(self):
        super().__init__()

    def turtle_play(self, dis, num, angle):    
        for i in range(int(num)):
            self.forward(dis)
            self.right(angle)

t1 = MyTurtle()

dis = turtle.numinput("거리 입력", "거리는?")
num = turtle.numinput("횟수 입력", "몇 번?")
angle = turtle.numinput("각도 입력", "각도는?")

t1.turtle_play(dis, num, angle)


turtle.exitonclick()