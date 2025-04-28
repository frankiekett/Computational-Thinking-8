import turtle
t = turtle.Turtle()

# setup
t.speed(10)
turtle.Screen().bgcolor("light blue")


# stripes

# move to stripe 1
t.goto(-250, -100)

H = 50 

# stripe 1
t.color("purple")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(H)
t.left(90)
t.forward(500)
t.left(90)
t.forward(H)
t.left(90)
t.end_fill()


# move to stripe 2
t.goto(-250, -50)

# stripe 2
t.color("blue")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(H)
t.left(90)
t.forward(500)
t.left(90)
t.forward(H)
t.left(90)
t.end_fill()

# move to stripe 3
t.goto(-250, 0)

# stripe 3
t.color("green")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(H)
t.left(90)
t.forward(500)
t.left(90)
t.forward(H)
t.left(90)
t.end_fill()

# move to stripe 4
t.goto(-250, 50)

# stripe 4
t.color("yellow")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(H)
t.left(90)
t.forward(500)
t.left(90)
t.forward(H)
t.left(90)
t.end_fill()

# move to stripe 5
t.goto(-250, 100)

# stripe 5
t.color("orange")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(H)
t.left(90)
t.forward(500)
t.left(90)
t.forward(H)
t.left(90)
t.end_fill()


t.goto(-250, 150)
# stripe 5
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(H)
t.left(90)
t.forward(500)
t.left(90)
t.forward(H)
t.left(90)
t.end_fill()








turtle.exitonclick()
