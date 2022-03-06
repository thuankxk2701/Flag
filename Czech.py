from turtle import *

speed(0)

setup(width=1000,height=600)


penup()
goto(-500,-300)
pendown()

color('firebrick')
begin_fill()
forward(1000)
left(90)
forward(300)
left(90)
forward(1000)
end_fill()

left(90)

penup()
goto(-500,300)
pendown()

color('navy')
begin_fill()
forward(594)
left(130)
forward(458)
end_fill()

hideturtle()
done()