#!/usr/bin/env python3

# Just some fun with turtle module

# Uses the Turtle module to draw a simple figure
import turtle

# Run
if __name__ == '__main__':
    # Create drawing board as well as set background and title
    db = turtle.Screen()
    db.bgcolor("light blue")
    db.title("My Turtle")

    # Create turtle
    max = turtle.Turtle()

    # Move turtle
    max.left(90)
    max.forward(100)
    max.right(90)
    max.circle(25,180)
    max.forward(40)
    max.circle(25,180)
    max.right(90)
    max.forward(100)
    max.right(90)
    max.forward(20)
    max.circle(50,225)
    max.right(90)
    max.circle(50,225)
    max.forward(20)

    # End drawing
    turtle.done()