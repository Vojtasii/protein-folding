import turtle

DEGREE = {'1': 0, '-1': 180, '1j': 90, '-1j': 270}
COLOR = {'1': 'dark orange', '0': 'turquoise'}
FONT = ('Trajan Pro', '10', 'normal')
L = 'left'
R = 'right'
C = 'center'

A = ((-45,-15), (-65, -45), (-105,-60)) # position for output on screen

def create_turtle(start = (0,0), color = 'black', angle = 0):
    """ Turtle setup """

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.speed(0)
    t.pencolor(color)
    t.setpos(start)
    t.seth(angle)
    return t

def create_window():
    """ Window setup """

    w = turtle.Screen()
    w.setup(800,1000,1000,10)
    w.title('< Title >')
    t1 = create_turtle((0, 350))
    t2 = create_turtle((-300, 300), 'grey')
    t3 = create_turtle((-300, -250), 'grey')
    t1.write('Protein folding', align=C, font=('Adobe Song Std L', '30', 'normal'))
    draw_line(t2, 600)
    draw_line(t3, 600)
    return w

def summon_ninja_turtles():
    """ Call for 6 main turtles that will be soon used in drawig output of protein folding on screen """

    global Terri, Lerri, Michelangelo, Raphael, Leonardo, Donatello
    Terri = create_turtle(color='grey')         # line maker
    Lerri = create_turtle()                     # dots placer
    Michelangelo = create_turtle((300, -245))   # prints the nnumber of protein
    Raphael = create_turtle((-300, -275))       # tells proteins length
    Leonardo = create_turtle((-300, -295))      # knows its energy
    Donatello = create_turtle()                 # can draw a 3d-effect-like arrow
    return Terri, Lerri, Leonardo, Michelangelo, Raphael, Donatello

def draw_conf(c, s):
    """ Draw a rotein folding on the screen """

    if Terri.isdown():
        Terri.penup()
    if Lerri.isdown():
        Lerri.penup()
    Terri.setpos(A[update_position(len(s))])
    Terri.pendown()
    for i, j in zip(c, s):
        Lerri.setpos(Terri.xcor(), Terri.ycor())
        draw_line(Terri, 20, DEGREE[i])
        Lerri.dot(10, COLOR[j])
    Terri.dot(10, COLOR[s[len(s) - 1]])

def update_text(num, length, energy=0):
    """ Self-explanatory """

    Michelangelo.write('{}.'.format(num), align=R, font=FONT)
    Raphael.write('length   {}'.format(length), align=L, font=FONT)
    Leonardo.write('energy    {}'.format(energy), align=L, font=FONT)

def draw_arrow():
    """ Self-explanatory """

    Donatello.penup()
    Donatello.setpos(285, -400)
    Donatello.seth(270)
    Donatello.pencolor(COLOR['0'])
    draw_triangle(Donatello, 20)
    Donatello.penup()
    Donatello.setpos(281, -400)
    Donatello.pencolor(COLOR['1'])
    draw_triangle(Donatello, 20)

def update_position(len_s):
    if 17 < len_s < 70:
        return 1
    elif len_s >= 70:
        return 2
    else:
        return 0

def draw_line(t, n, d = 0):
    t.seth(d)
    if not t.isdown():
        t.pendown()
    t.forward(n)

def draw_triangle(t, n):
    if not t.isdown():
        t.pendown()
    for i in range(3):
        t.forward(n)
        t.lt(120)