import turtle
import os
import shutil
import tempfile

def display(file):
    w = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.setpos(-256,256)
    t.pendown()
    with open(file, 'rt', encoding='utf-8') as f:
        for line in f:
            l = list(line.split())
            for i in l:
                t.rt(-90)
                if i == '1':
                    #print('*', end=' ')
                    t.begin_fill()
                    t.circle(5)
                    t.end_fill()
                else:
                    #print('o', end=' ')
                    t.circle(5)
                t.rt(90)
                t.forward(20)
                t.penup()
                t.setpos(t.xcor() + 10, t.ycor())
                t.pendown()
            t.penup()
            t.setpos(-256, t.ycor() - 20)
            t.pendown()
            #print('\n')
    ts = t.getscreen()
    ts.getcanvas().postscript(file='proteins.eps')
    w.exitonclick()

if __name__ == '__main__':
    display('folding.txt')

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