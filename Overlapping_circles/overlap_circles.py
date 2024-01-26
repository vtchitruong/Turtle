import turtle

if __name__ == '__main__':
    s = turtle.getscreen() # init screen
    p = turtle.Turtle() # init pen

    turtle.bgcolor('black')
    # turtle.Screen().bgcolor('black')

    p.width(3) # width() is an alias for pensize()
    p.speed(0) # super fast
    p.color('#32cd32') # lime green

    for _ in range(50):
        p.circle(200) # radius
        p.right(50) # 50 degrees to the right

    p.screen.mainloop() # pause for viewing