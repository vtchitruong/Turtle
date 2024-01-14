import turtle

if __name__ == '__main__':
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

    # Init screen
    s = turtle.getscreen()
    turtle.Screen().bgcolor('black')

    # Init pen
    p = turtle.Turtle()

    # Set speed of pen to super fast
    p.speed(0)

    for x in range(360):
        # Set 6 different colors to 6 edges
        p.pencolor(colors[x % 6])

        # Set pen size from thin to thick
        p.width(x // 100)

        # Draw 1 edge
        p.forward(x)

        # Turn left by 60 degrees for spiral effect
        p.left(61)

    # Pause for viewing
    p.screen.mainloop()