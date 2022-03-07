from turtle import *
speed(0)
ht()
setup(width=1000,height=600)
bgcolor('red')

def start(size):
    # color('yellow')
    # begin_fill()
    for i in range(0,4):
        forward(size)
        right(144)
    # end_fill()    
penup()
goto(0,0)
pendown()

start(120)
done()