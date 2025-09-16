from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
xvector = 1
yvector = 0
rotate = -89
Origin = (400, 300)
flag = True

while True:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)

    if flag:
        x += xvector * 10
        y += yvector * 10
    else:
        x = Origin[0] + (math.cos(math.radians(rotate)) * 230)
        y = Origin[1] + 20 + (math.sin(math.radians(rotate)) * 230)
        rotate += 1

    if flag:
        if x >= 800 - 20 and y <= 90:
            x = 780
            xvector = 0
            yvector = 1
        elif x >= 800 - 20 and y >= 600 - 40:
            y = 600 - 40
            xvector = -1
            yvector = 0
        elif x <= 20 and y >= 600 - 40:
            x = 20
            xvector = 0
            yvector = -1
        elif x <= 20 and y <= 90:
            y = 90
            xvector = 1
            yvector = 0
        elif x == 400 and y == 90:
            flag = False
            xvector = 1
            yvector = 0
    else:
        if rotate == 270:
            flag = True
            rotate = -89
            x = 400
            y = 90


    delay(0.01)

close_canvas()
