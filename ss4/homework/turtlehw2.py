from turtle import*
shape('turtle')
speed(-1)
color('blue')
right(120)
for j in range(50):
    for i in range(4):
        forward(100 - 2*j)
        right(90)
    right(10)
mainloop()
