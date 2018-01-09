import turtle
import tkinter
import os
import shutil
import tempfile

def display(sequences, configurations):
    w = turtle.Screen()
    w.getcanvas()
    w.setup(600,600,0,0)
    t = turtle.Turtle()
    t.penup()
    t.setpos(-280,260)
    t.speed(0)
    m = 0
    p = 0
    with open(sequences, 'rt', encoding='utf-8') as s:
        with open(configurations, 'rt', encoding='utf-8') as c:
            for seq, conf in zip(s, c):
                cf = list(conf.split())
                sq = list(seq.split())
                for i, j in zip(sq, cf):
                    if i == '1':
                        t.dot(10, 'blue')
                    else:
                        t.dot(10, 'red')
                    if j == '-1j':
                        t.seth(270)
                        t.forward(20)
                    elif j == '1j':
                        t.seth(90)
                        t.forward(20)
                    elif j == '-1':
                        t.seth(180)
                        t.forward(20)
                    else:
                        t.seth(0)
                        t.forward(20)
                if sq[len(sq) - 1] == '1':
                    t.dot(10, 'blue')
                else:
                    t.dot(10, 'red')
                m += 1
                t.penup()
                if m == 6:
                    p += 1
                    m = 0
                t.setpos(-280 + 100*m, 260 - 100*p)
                t.pendown()
    print(t.pos())
    w.exitonclick()

if __name__ == '__main__':
    display('sequences_public.txt','folding.txt')

'''
    w = turtle.Screen()
    t = turtle.Turtle()
    t.rt(-90)
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.rt(90)
    t.forward(20)
    t.penup()
    t.setpos(t.xcor() + 10, 0)
    t.rt(-90)
    t.pendown()
    t.circle(5)
    t.rt(90)
    t.forward(20)
    t.penup()
    t.setpos(t.xcor()+5, t.ycor()+5)
    t.rt(-180)
    t.pendown()
    t.circle(5)
    t.rt(90)
    t.forward(20)
    t.penup()
    t.setpos(t.xcor()-5, t.ycor()+5)
    t.rt(-180)
    t.pendown()
    t.circle(5)
    t.rt(90)
    t.forward(20)
    t.penup()
    t.setpos(t.xcor() - 10, t.ycor())
    t.rt(-90)
    t.pendown()
    t.circle(5)
    t.rt(90)
    t.forward(20)
    t.penup()
    t.setpos(t.xcor() - 10, t.ycor())
    t.rt(-90)
    t.pendown()
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    w.exitonclick()
'''