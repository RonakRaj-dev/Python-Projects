import turtle

# Set up the turtle window
window = turtle.Screen()
window.bgcolor("purple")

# Create a turtle object
heart = turtle.Turtle()
heart.speed(2)  # Set the speed of the turtle (optional)

# Set the color of the turtle
heart.color("red")

# Start drawing the heart shape
heart.begin_fill()
heart.left(140)

# Draw the outer curve of the heart
heart.forward(180)
heart.circle(-90, 200)

# Move to the top of the heart
heart.left(120)
heart.circle(-90, 200)

# Draw the inner curve of the heart
heart.forward(180)

# End filling the heart shape
heart.end_fill()

# Hide the turtle
heart.hideturtle()

# Keep the turtle window open
turtle.done()
