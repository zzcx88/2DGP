from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 0
move_range = 5
frame = 0
bottom = 100
switch = 0
while (True):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, bottom, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    x += move_range
    if x == 800:
        move_range = -5
        bottom = 0
    if x == 0:
        move_range = 5
        bottom = 100
    delay(0.05)
    get_events()

close_canvas()

