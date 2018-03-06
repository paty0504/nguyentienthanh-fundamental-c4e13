
from turtle import *

shape('turtle')
speed(-1)
color('yellow')
begin_fill()
#draw a square
for i in range(4):
 forward(100)
 left(90)
#
#draw a circle
circle(100)
###
#draw a right triagle
for i in range(3):
    forward(100)
    left(120)
##
#draw a multicircle
for i in range(12):
    circle(100)
    right(60)
##
end_fill()
mainloop()
