import turtle

SEQ_DIR = 'sequences.txt'
CONF_DIR = 'folding.txt'

A = (0,-100)

B = [(-150,50), (150,50), (-150,-250), (150,-250)]

C = [(-225,125), (-75,125), (75,125), (225,125),
     (-225,-25), (-75,-25), (75,-25), (225,-25),
     (-225,-175), (-75,-175), (75,-175), (225,-175),
     (-225,-325), (-75,-325), (75,-325), (225,-325)]

degree = {'1': 0, '-1': 180, '1j': 90, '-1j': 270}
color = {'1': 'dark orange', '0': 'turquoise'}


def setup_window():
    t_start = turtle.Turtle()
    t_start.hideturtle()
    t_start.speed(0)
    w = turtle.Screen()
    w.setup(800,1000,1000,10)
    w.title('< Title >')
    t_start.penup()
    t_start.setpos(0, 350)
    t_start.write('Protein Folding', align='center', font=('Adobe Song Std L', '30', 'normal'))
    t_start.setpos(-300,300)
    t_start.pendown()
    t_start.forward(600)
    return w


def display(config, sequences):
    w = setup_window()

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    n = 0

    with open(config, 'rt', encoding='utf-8') as f, \
            open(sequences, 'rt', encoding='utf-8') as f2:
        for config, seq in zip(f, f2):
            c = config.split()
            s = seq.split()
            t.penup()
            if 8 < len(s) < 32:
                if n > 3:
                    n = 0
                    t.clear()
                t.setpos(B[n])
                m = 3
            elif len(s) >= 32:
                if n > 0:
                    n = 0
                    t.clear()
                t.setpos(A)
                m = 0
            else:
                t.setpos(C[n])
                m = 15
            t.pendown()
            #w.tracer(0,0)
            for i, j in zip(c, s):
                t.dot(10, color[j])
                t.seth(degree[i])
                t.forward(20)
            t.dot(10, color[s[len(s) - 1]])
            #w.update()
            if n == m:
                n = 0
                t.clear()
            else:
                n += 1
    w.exitonclick()


if __name__ == '__main__':
    display(CONF_DIR, SEQ_DIR)
