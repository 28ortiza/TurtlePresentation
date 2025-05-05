import turtle
import random

screen = turtle.Screen()
screen.screensize(canvwidth=500, canvheight=500)
screen.bgcolor("DarkSlateGray1")
t=turtle.Turtle()
t.speed(0)

#intro screen
t.penup()
t.goto(0, 100)
t.pendown()
t.write("Aalayah", font=("Arial", 30, "italic"), align="center")

t.penup()
t.goto(-100, 0)
t.pendown()
screen.addshape('friends.gif')
t.shape('friends.gif')
t.stamp()
t.shape("classic")
t.penup()
t.goto(100, 0)
t.pendown()
screen.addshape('sunset.gif')
t.shape('sunset.gif')
t.stamp()
t.shape("classic")


t.penup()
t.goto(0, -100)
t.pendown()
t.write("Ortiz", font=("Arial", 30, "italic"), align="center")
# flower drawing
t.penup()
t.goto(0,50)
t.pendown()
t.pencolor('green')
t.pensize(8)
t.goto(0,-50)
t.pensize(1)
t.penup()
t.goto(0,50)
t.pendown()

t.pencolor('pink')
t.fillcolor('pink')
t.begin_fill()
t.circle(25)
t.setheading(90)
t.circle(25)
t.setheading(180)
t.circle(25)
t.setheading(270)
t.circle(25)
t.end_fill()
t.penup()
t.goto(0,33)
t.pendown()
t.setheading(0)
t.fillcolor('yellow')
t.begin_fill()
t.circle(15)
t.end_fill()

t.pencolor('DarkSlateGray4')
t.penup()
t.goto(0, -350)
t.pendown()
t.write("Press Enter To Continue", font=("Arial", 30, "italic"), align="center")

round = input("Press Enter To Continue: ")
t.clear()


# page2
screen.bgcolor("MediumPurple")
t.pencolor('white')
t.penup()
t.goto(0, 250)
t.pendown()
t.write("My Favorite Foods", font=("Arial", 30, "italic bold"), align="center")

t.penup()
t.goto(0, 100)
t.pendown()
t.write("1. Alfredo", font=("Arial", 30, "italic"), align="center")
t.penup()
t.goto(0, 0)
t.pendown()
t.write("2. Tropical Smoothie ", font=("Arial", 30, "italic"), align="center")
t.penup()
t.goto(0, -100)
t.pendown()
t.write("3. Spaghetti", font=("Arial", 30, "italic"), align="center")

# pictures
t.penup()
t.goto(-100, -200)
t.pendown()
screen.addshape('alfredo.gif')
t.shape('alfredo.gif')
t.stamp()
t.shape("classic")
t.penup()
t.goto(100, -200)
t.pendown()
screen.addshape('food.gif')
t.shape('food.gif')
t.stamp()
t.shape("classic")

t.pencolor('MediumPurple4')
t.penup()
t.goto(0, -350)
t.pendown()
t.write("Press Enter To Continue", font=("Arial", 30, "italic"), align="center")

# drawings
t.penup()
t.pencolor('MediumPurple4')
t.fillcolor('MediumPurple4')
t.goto(-250,100)
t.pendown()
t.begin_fill()
octogon = t
sides = 8
length = 50
angle = 360/sides

for i in range(sides):
    octogon.forward(length)
    octogon.left(angle)
t.penup()
t.end_fill()

round = input("Press Enter To Continue: ")
t.clear()

# page 3
screen.bgcolor("DarkSeaGreen")
t.pencolor('white')
t.penup()
t.goto(0, 250)
t.pendown()
t.write("My Hobbies", font=("Arial", 30, "italic bold"), align="center")

t.penup()
t.goto(0, 150)
t.pendown()
t.write("1. Hanging out with friends", font=("Arial", 30, "italic"), align="center")
t.penup()
t.goto(0, 50)
t.pendown()
t.write("2. Doing my nails ", font=("Arial", 30, "italic"), align="center")
t.penup()
t.goto(0, -50)
t.pendown()
t.write("3. Sleeping", font=("Arial", 30, "italic"), align="center")
t.penup()
t.goto(0, -150)
t.pendown()
t.write("3. Tanning", font=("Arial", 30, "italic"), align="center")

# pictures
t.penup()
t.goto(-100, -220)
t.pendown()
screen.addshape('frends.gif')
t.shape('frends.gif')
t.stamp()
t.shape("classic")
t.penup()
t.goto(100, -220)
t.pendown()
screen.addshape('nails.gif')
t.shape('nails.gif')
t.stamp()
t.shape("classic")

# drawing
t.penup()
t.pencolor('DarkOliveGreen4')
t.goto(-250,250)
t.pendown()
spiral = t
for i in range(50):
    spiral.forward(i)
    spiral.left(40)
t.penup()

t.pencolor('DarkSeaGreen4')
t.penup()
t.goto(0, -350)
t.pendown()
t.write("Press Enter To Continue", font=("Arial", 30, "italic"), align="center")

round = input("Press Enter To Continue: ")
t.clear()

# page 3
screen.bgcolor("violet")
t.pencolor('white')
t.penup()
t.goto(0, 250)
t.pendown()
t.write("My Favorite Movie", font=("Arial", 30, "italic bold"), align="center")

t.penup()
t.goto(0, 100)
t.pendown()
t.write("How To Lose A Guy in 10 Days", font=("Arial", 30, "italic"), align="center")



# pictures
t.penup()
t.goto(-100, 0)
t.pendown()
screen.addshape('how.gif')
t.shape('how.gif')
t.stamp()
t.shape("classic")
t.penup()
t.goto(100, 0)
t.pendown()
screen.addshape('10days.gif')
t.shape('10days.gif')
t.stamp()
t.shape("classic")
# drawing
t.penup()
t.pencolor('yellow')
t.fillcolor('yellow')
t.goto(50,-150)
t.pendown()
t.begin_fill()
star = t
for i in range(5):
    star.forward(100)
    star.right(144)
t.penup()
t.end_fill()

t.pencolor('VioletRed')
t.penup()
t.goto(0, -350)
t.pendown()
t.write("Press Enter To Continue", font=("Arial", 30, "italic"), align="center")

round = input("Press Enter To Continue: ")
t.clear()

# page 4
screen.bgcolor("SteelBlue3")
t.pencolor('white')
t.penup()
t.goto(0, 250)
t.pendown()
t.write("My Favorite Sport", font=("Arial", 30, "italic bold"), align="center")

t.penup()
t.goto(0, 100)
t.pendown()
t.write("Volleyball", font=("Arial", 30, "italic"), align="center")


# pictures
t.penup()
t.goto(-100, 0)
t.pendown()
screen.addshape('volleyball.gif')
t.shape('volleyball.gif')
t.stamp()
t.shape("classic")
t.penup()
t.goto(100, 0)
t.pendown()
screen.addshape('vb.gif')
t.shape('vb.gif')
t.stamp()
t.shape("classic")

# drawing
t.penup()
t.pencolor('steelblue4')
t.fillcolor('steelblue4')
t.fillcolor('steelblue4')
t.goto(50,-150)
t.pendown()
t.begin_fill()
for i in range(6):
    t.forward(100)
    t.left(60)
t.pendown()
t.end_fill()

turtle.done()