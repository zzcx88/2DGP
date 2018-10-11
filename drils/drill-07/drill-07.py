from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
frame = 0

size = 20
points = [(random.randint(-500, 500), random.randint(-350, 350)) for i in range(size)]
n = 1

def draw_line(p1, p2):
    global x, y
    for i in range(0, 100 + 1, 2):
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
x1 = 0
y1 = 0
while True:
    draw_line(points[n - 1], points[n])
    while x != x1 and y != y1:
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        if x <= x1 and y < y1:
            x += 1
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        clear_canvas()
        delay(0.02)
    update_canvas()
    frame = (frame + 1) % 8
    n = (n + 1) % size
close_canvas()