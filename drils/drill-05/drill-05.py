from pico2d import *
open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def move_to_132_243():
    # character's defaultcordinate
    x = 800 // 2
    y = 0 + 60
    frame = 0
    bottom = 0
    while x > 132 and y < 243:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, bottom, 100, 100, x, y)
        frame = (frame + 1) % 8
        update_canvas()
        x -= 2
        y += 2
        delay(0.05)

def move_to_435_470():
    x = 132
    y = 243
    frame = 0
    bottom = 100
    while x < 435 and y < 470:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, bottom, 100, 100, x, y)
        frame = (frame + 1) % 8
        update_canvas()
        x += 2
        y += 2
        delay(0.05)
def move_to_477_203():
    x = 435
    y = 470
    frame = 0
    bottom = 100
    while x < 477 and y > 203:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, bottom, 100, 100, x, y)
        frame = (frame + 1) % 8
        update_canvas()
        x += 2
        y -= 2
        delay(0.05)
def move_to_715_136():
    x = 477
    y = 203
    frame = 0
    bottom = 100
    while x < 715 and y > 136:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, bottom, 100, 100, x, y)
        frame = (frame + 1) % 8
        update_canvas()
        x += 2
        y -= 2
        delay(0.05)
def move_to_316_225():
    x = 715
    y = 136
    frame = 0
    bottom = 0
    while x > 316 and y < 225:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, bottom, 100, 100, x, y)
        frame = (frame + 1) % 8
        update_canvas()
        x -= 2
        y += 2
        delay(0.05)
def move_to_510_92():
    pass
def move_to_692_518():
    pass
def move_to_682_336():
    pass
def move_to_712_349():
    pass

def move_to_cordinate():
    #move_to_132_243()
    #move_to_435_470()
    #move_to_477_203()
    #move_to_715_136()
    move_to_316_225()
    #move_to_510_92()
    #move_to_692_518()
    #move_to_682_336()
    #move_to_712_349()
while True:
    move_to_cordinate()

close_canvas()
