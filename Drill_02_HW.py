from pico2d import*
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png');

x = 400
y = 90
cnt = 0
rad = 250
angle = 2
n = 0.1
circle = 1
while (True):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    if x == 400 and y == 90:
        if circle:
            circle = 0
        else:
            circle = 1
        n = 1
    if circle:
        x = rad * math.cos(2 * math.pi * 3/4 -  n) + 400
        y = rad * math.sin(2 * math.pi * 3/4 - n) + 340
        n += 0.1
        if n >= 2 * math.pi:
            circle = 0
            x = 405
            y = 90
        delay(0.05)
    else:
        if x < 800 and y == 90:
            x += 5
        elif x == 800 and y < 600:
            y += 5
        elif x == 0 and y <= 600:
            y -= 5
        elif x <= 800 and y >= 600:
            x -= 5
        delay(0.01)