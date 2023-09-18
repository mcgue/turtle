#!/usr/bin/env python3

# Uses the Turtle module to draw

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
    max.forward(50)
    max.right(50)
    max.forward(50)

    # End drawing
    turtle.done()