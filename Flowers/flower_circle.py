import turtle

s = turtle.getscreen() # init screen
p = turtle.Turtle() # init pen

p.width(3) # width() is an alias for pensize()
p.speed(0) # super fast
p.color('#ffeb0f') # yellow

for _ in range(36):
    # draw the lower stroke
    p.circle(radius=200, extent=90) # a 90 degrees arc
    
    # draw an upper stroke
    p.left(100)    
    p.circle(radius=200, extent=90) # a 90 degrees arc

    p.left(10)

p.screen.mainloop() # pause for viewing