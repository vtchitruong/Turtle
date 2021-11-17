import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.width(3) # width() is an alias for pensize()
t.speed(0)
t.color('blue')

for x in range(50):
    t.circle(200)
    t.right(50)

t.screen.mainloop()