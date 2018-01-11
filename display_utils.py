import turtle

DEGREE = {'1': 0, '-1': 180, '1j': 90, '-1j': 270}
COLOR = {'1': 'dark orange', '0': 'turquoise'}
FONT = ('Trajan Pro', '10', 'normal')
L = 'left'
R = 'right'
C = 'center'

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

def setup_window():
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

def draw_arrow():
    t = create_turtle((285, -400), COLOR['0'], 270)
    draw_triangle(t, 20)
    t.penup()
    t.setpos(281, -400)
    t.pencolor(COLOR['1'])
    draw_triangle(t, 20)
    return t

def update_text(num, length, energy = 0):
    t1 = create_turtle((300, -245))
    t2 = create_turtle((-300, -275))
    t3 = create_turtle((-300, -295))
    t1.write('{}.'.format(num), align=R, font=FONT)
    t2.write('length {}'.format(length), align=L, font=FONT)
    t3.write('energy {}'.format(energy), align=L, font=FONT)
    return t1, t2, t3

