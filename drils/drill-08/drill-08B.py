from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH, KPU_HEIGHT)
Ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

frame = 0
size = 10
points = [(random.randint(300, 600), random.randint(300, 600)) for i in range(size)]
n = 3

def draw_curve(p1, p2, p3):
    pass

while True:
    x, y = points[n-1]
    tx, ty = points[n]
    clear_canvas()
    i = 0
    while tx != x and y != ty:
        print(points)
        clear_canvas()
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * points[n-3][0] + (3 * t ** 3 - 5 * t ** 2 + 2) * points[n-2][0] + (-3 * t ** 3 + 4 * t ** 2 + t) * points[n-1][0] + (t ** 3 - t ** 2) * points[n][0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * points[n-3][1] + (3 * t ** 3 - 5 * t ** 2 + 2) * points[n-2][1] + (-3 * t ** 3 + 4 * t ** 2 + t) * points[n-1][1] + (t ** 3 - t ** 2) * points[n][1]) / 2
        i += 2
        Ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
    n += 1
    get_events()

close_canvas()

