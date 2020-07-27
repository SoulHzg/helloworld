import turtle

turtle.pensize(3)
turtle.circle(100)
turtle.color("black")

turtle.penup()#拿起笔
turtle.goto(-200,0)
turtle.color("blue")
turtle.pendown()#放下笔
turtle.circle(100)

turtle.penup()
turtle.goto(200,0)
turtle.color("red")
turtle.pendown()
turtle.circle(100)

turtle.penup()
turtle.goto(-100,-100)
turtle.color("yellow")
turtle.pendown()
turtle.circle(100)

turtle.penup()
turtle.goto(100,-100)
turtle.color("green")
turtle.pendown()
turtle.circle(100)
turtle.done()#停止画笔绘制，绘图窗口不关闭
