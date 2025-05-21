# Section 1 - Helper functions
import turtle, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def create_sprite(image_filename, x=0, y=0):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite = turtle.Turtle()
	sprite.shape(image_file)
	sprite.penup()
	sprite.goto(x,y)
	return sprite


# Section 2 - Variables
x1 = 200
y1 = -200
x2 = 150
y2 = -100
x3 = -100
y3 = 200
x4 = 50
y4 = 100
# Section 3 - Setup

set_background("summer")
t1 = create_sprite("basketball",x1,y1)
t2 = create_sprite("kitten",x2,y2)
t3 = create_sprite("bat",x3,y3)
t4 = create_sprite("flower",x4,y4)


# # Section 4 -what sprites are faster and slower 
# sprite one is the slowest because the average of the random numbers is the smallest 
# sprite 2 is the fastest because the average of there numbers (the speed) is the largest

for i in range(30):
	x1 += random.randint(7, 10)
	x2 += random.randint(12,17)
	x3 += random.randint(13,14)
	x4 += random.randint(11,16)
	t1.goto(x1, y1)
	t2.goto(x2, y2)
	t3.goto(x3, y3)
	t4.goto(x4, y4)
	time.sleep(0.1)


# # Section 5 - Winner

if x1 >= x2 and x1 >= x3 and x1 >= x4:
 	print("basketball wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
 	print("kitten wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
	print("bat wins!")
elif x4 >= x1 and x4 <= x2 and x4 >= x4:
	print("flower wins!")




turtle.exitonclick()


