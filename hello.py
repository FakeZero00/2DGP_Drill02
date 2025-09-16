from pico2d import *

open_canvas()

img = load_image('character.png')

img.draw_now(20, 40)

delay(5)

close_canvas()