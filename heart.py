import turtle as t
import time

p = t.Turtle()

def curve():
    for i in range(200):
        p.right(1)
        p.forward(1)

def text():
    p.up()
    p.setpos(-45, 90)
    p.down()
    p.color('lightgreen')
    p.write('abcdefgh', font=('Verdana', 12, 'bold'))

def heart():
    p.fillcolor('red')
    p.begin_fill()
    p.left(140)
    p.forward(113)
    curve()
    p.left(120)
    curve()
    p.forward(112)
    p.end_fill()

heart()
text()
p.ht()
time.sleep(3)
print('Done')
