import turtle as tl

def draw_fractal(size):
    if size >= 8:
        tl.pensize(max(size / 50, 1))
        tl.forward(size)
        tl.left(45)
        draw_fractal(size / 2.5)
        tl.right(90)
        draw_fractal(size / 2.5)
        tl.left(45)
        draw_fractal(size / 1.5)
        tl.penup()
        tl.backward(size)
        tl.pendown()
    else:
        tl.pensize(3)

size = 100
tl.delay(1)
tl.speed(0)
tl.penup()
tl.color('blue')
tl.pendown()

for i in range(1,8):
    draw_fractal(size)
    tl.setheading(i*45)
draw_fractal(size)
tl.done()