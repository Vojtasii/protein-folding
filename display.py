from display_utils import *
import time

SEQ_DIR = 'sequences.txt'
CONF_DIR = 'folding.txt'

A = ((-45,-15), (-65, -45), (-105,-60))

def draw_conf(t, d, c, s):
    t.pendown()
    for i, j in zip(c, s):
        d.setpos(t.xcor(),t.ycor())
        draw_line(t, 20, DEGREE[i])
        d.dot(10, COLOR[j])
    t.dot(10, COLOR[s[len(s) - 1]])

def clear_screen(x, y):
    pass

def display(config, sequences):
    w = setup_window()
    line = create_turtle(color='grey')
    dot = create_turtle()

    global counter
    counter = 0
    pos = 0

    with open(config, 'rt', encoding='utf-8') as f, \
            open(sequences, 'rt', encoding='utf-8') as f2:
        for conf, seq in zip(f, f2):
            counter += 1
            c = conf.split()
            s = seq.split()
            #w.tracer(0,0)

            # ... inputting
            p = update_text(counter, len(s))
            line.penup(), dot.penup()
            if 17 < len(s) < 70:
                pos = 1
            elif len(s) >= 70:
                pos = 2
            line.setpos(A[pos])
            draw_conf(line, dot, c, s)
            time.sleep(.2)
            a = draw_arrow()
            #w.update()
            time.sleep(.5)

            # ... cleaning
            line.clear()
            dot.clear()
            p[0].clear(), p[1].clear(), p[2].clear()
            a.clear()

    w.exitonclick()


if __name__ == '__main__':
    display(CONF_DIR, SEQ_DIR)

'''
B = [(-150,50), (150,50), (-150,-250), (150,-250)]

C = [(-225,125), (-75,125), (75,125), (225,125),
     (-225,-25), (-75,-25), (75,-25), (225,-25),
     (-225,-175), (-75,-175), (75,-175), (225,-175),
     (-225,-325), (-75,-325), (75,-325), (225,-325)]

D = [(-25,25), (-25,-325)]

E = [(-225,50), (-75,50), (75,50), (225,50),
     (-225,-325), (-75,-325), (75,-325), (225,-325)]

F = [(-225,25), (75,25),
     (-225,-325), (75,-325)]
'''