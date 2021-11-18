import turtle

s = turtle.getscreen() # init screen
t = turtle.Turtle() # init pen

t.width(3) # width() is an alias for pensize()
t.speed(0) # super fast
t.color('#32cd32') # lime green

for _ in range(50):
    t.circle(200) # radius
    t.right(50) # 50 degrees to the right

t.screen.mainloop() # pause for viewing