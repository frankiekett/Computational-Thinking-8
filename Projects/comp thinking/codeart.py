# setup
import turtle

t = turtle.Turtle()
# where to go and other colors for it 
t.goto(-100,0)
t.color("pink")
turtle.Screen().bgcolor("black")
t.speed(10)

# making the art 
colors = ["blue","purple","cyan"]
for i in range(1000):
    t.color( colors[ i %3])
    t.forward(300)
    t.left(251)


turtle.exitonclick 
