import game_framework
from pico2d import *


name = "PauseState"
image = None


def enter():
    global image
    image = load_image('pause_new.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                resume()


global time
time = 0
def draw():
    global time
    time += 1
    delay(0.3)

    #pass


def update():
    if  time % 2 == 0:
        game_framework.stack[-2].pause()
        image.draw(400,300)
        update_canvas()
    else:
        clear_canvas()
        game_framework.stack[-2].pause()
        update_canvas()


def pause():
    pass


def resume():
    game_framework.pop_state()

