from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH, KPU_HEIGHT)
Ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

size = 10
points = [(random.randint(0, 1200), random.randint(0, 1000)) for i in range(size)]
n = 0
def draw_curve(p1,p2,p3,p4):
    i = 0
    frame = 0
    x = 0
    for i in range(0, 100, 2):
        t = i / 100
        prveX = x
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) *
             p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) *
             p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
        clear_canvas()
        Ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        if x <= prveX:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
        else:
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
while True:
    draw_curve(points[n], points[n+1], points[n+2], points[n+3])
    n += 1
    if (n+3) == 9:
        n = 0
    get_events()

close_canvas()

