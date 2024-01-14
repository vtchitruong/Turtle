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

    for x in range(10, 120):
        # Set yellow to all edges
        p.pencolor(colors[2])

        # Set pen size from thin to thick 
        p.width(x // 100)        
        
        for _ in range(8):
            # Draw 1 edge
            p.forward(x)
            
            # Turn left by 45 degrees for octagon
            p.left(45)
        
        # Turn left by 60 degrees for spiral effect
        p.left(10)

    # Pause for viewing
    p.screen.mainloop()