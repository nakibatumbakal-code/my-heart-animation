
import turtle
import time

# Create the window
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("#101020")
screen.title("A Special Heart")
screen.tracer(0)

# Create the heart turtle
heart = turtle.Turtle()
heart.hideturtle()
heart.speed(0)
heart.color("#ff3366")
heart.pensize(3)

# Draw the heart
heart.penup()
heart.goto(0, -100)
heart.pendown()
heart.begin_fill()
heart.setheading(140)
heart.forward(180)
heart.circle(-90, 200)
heart.setheading(60)
heart.circle(-90, 200)
heart.forward(180)
heart.end_fill()

# Create the text turtle
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color("white")

# Text animation
message = "YOU ARE SPECIAL"

writer.goto(0, -220)

for letter in message:
    writer.write(letter, align="center",
                 font=("Arial", 22, "bold"))
    screen.update()
    time.sleep(0.15)

# Keep window open
screen.update()
turtle.done()
