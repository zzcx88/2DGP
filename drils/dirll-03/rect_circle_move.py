from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400, 30)
character.draw_now(400,90)

switch = 0;

x = 400
y = 90
radius = 250
pi = math.pi
n = pi/180
while (True):
    for degree in range(0, 360):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = radius * math.sin(degree * n) + 400
        y = radius * math.cos(degree * n) + 340
        delay(0.01)
    switch = 1;
    y = 90
    if (switch == 1):
        while ( x <= 800):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, 90)
            x = x + 1
            delay(0.001)
        while ( y <= 600):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y = y + 1;
            delay(0.001)
        while (x >= 0):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x = x - 1
            delay(0.001)
        while (y > 90):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y = y - 1
            delay(0.001)
        while ( x <= 400):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x = x + 1
            delay(0.001)
    switch = 0
close_canvas()
