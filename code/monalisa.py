import turtle

# Set the window size to 600x600 pixels
turtle.setup(600, 600)

# Create a turtle object
t = turtle.Turtle()

# Set the turtle's shape to "arrow"
t.shape("arrow")

# Set the turtle's speed to the maximum value (10)
t.speed(10)

# Set the turtle's color to light blue
t.color("light blue")

# Draw the head
t.penup()
t.goto(-100,100)
t.pendown()
t.circle(100)

# Draw the left eye
t.penup()
t.goto(-60,60)
t.pendown()
t.circle(20)

# Draw the right eye
t.penup()
t.goto(-140,60)
t.pendown()
t.circle(20)

# Draw the mouth
t.penup()
t.goto(-100,20)
t.pendown()
t.circle(80,180)

# Hide the turtle
t.hideturtle()

# Keep the window open until it is closed
turtle.mainloop()
