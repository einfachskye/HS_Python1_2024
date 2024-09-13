import turtle




# length = 1000

# turtle.forward(length)
# turtle.left(90) # turn left 90
# turtle.forward(length)
# turtle.left(90)
# turtle.forward(length)
# turtle.left(90)

turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.begin_fill()
turtle.color("pink")
turtle.circle(100)
turtle.end_fill()
turtle.penup()
turtle.goto(-70, 40)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()
turtle.fillcolor("#F3E5AB")
turtle.setheading(45)
turtle.forward(50)
turtle.setheading(135)
turtle.forward(50)
turtle.setheading(270)
turtle.forward(70)
turtle.end_fill()

turtle.begin_fill()
turtle.color("black")
turtle.end_fill()
turtle.circle(30)
turtle.penup()
turtle.goto(0,0)

turtle.penup()
turtle.goto(70, 40)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#F3E5AB")
turtle.setheading(135)
turtle.forward(50)
turtle.setheading(45)
turtle.forward(50)
turtle.setheading(270)
turtle.forward(70)
turtle.end_fill()

turtle.circle(-30)
turtle.penup()
turtle.goto(0,0)

turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.end_fill()
turtle.circle(8)
turtle.circle(0)
turtle.penup()
turtle.circle(-40)

turtle.penup()
turtle.goto(-20, -60)
turtle.setheading(-60)
turtle.pendown()
turtle.circle(20,120)








turtle.mainloop()


