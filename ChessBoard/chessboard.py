import turtle 

s = turtle.getscreen() # init screen
p = turtle.Turtle() # init pen


# Draw a cell
def draw_cell():
    for e in range(4):
        # move the pen forward 50 units
        p.forward(50)

        # turn left for the next edge
        p.left(90)
    
    # move the pen forward 50 units after finish a cell
    p.forward(50)


# Draw a row of 8 cells
def draw_row(r):
    for c in range(8):
        # change color for each cell
        if (r + c) % 2 == 0:
            cell_color = '#ffaa00' # can be 'black'
        else:
            cell_color = '#f2f2f2' # can be 'white'
        
        # set fill color for the cell
        p.fillcolor(cell_color)
        p.pencolor('#ffaa00')

        # start filling the cell with cell_color
        p.begin_fill()

        # call the draw_cell function
        draw_cell()
        p.end_fill()


# Draw the board of 8 rows
def draw_board():
    for r in range(8):

        # lift up the pen, not to draw    
        p.up()

        # set the position of the pen
        p.setpos(-200, 50 * r - 200)

        # start drawing again
        p.down()

        draw_row(r)


if __name__ == '__main__':
    p.speed(0)

    # set screen size
    s.setup(600, 600) 
    
    draw_board()

    # hide the pen
    p.hideturtle()

    # pause for viewing
    p.screen.mainloop()