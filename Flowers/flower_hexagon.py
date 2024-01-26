import turtle

if __name__ == '__main__':
    s = turtle.getscreen() # init screen
    t = turtle.Turtle() # init pen

    t.width(3) # width() is an alias for pensize()
    t.speed(0) # super fast
    t.color('cyan')
    turtle.bgcolor('black') 

    for i in range(18):
        t.circle(180, steps=6) # draw hexagon
        t.right(100) # turn right by 100 degrees

    t.screen.mainloop() # pause for viewing