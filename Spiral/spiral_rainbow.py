import turtle
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

s = turtle.getscreen() # init screen
turtle.Screen().bgcolor('black')

t = turtle.Turtle() # init pen

t.speed(0) # super fast

for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x // 100 + 1)
    t.forward(x)
    t.left(59)

t.screen.mainloop() # pause for viewing
