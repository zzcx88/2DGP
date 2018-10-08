from pico2d import *
import random

# Game object class here
class Ball:
    def __init__(self):
        ini = random.randint(0, 20)
        if ini % 2 == 0:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')
        self.y = 700
        self.x = random.randint(0,700)
        self.fallSpeed = random.randint(1,10)
    def update(self):
        if self.y <= 80:
            self.y = 80
        else:
            self.y -= self.fallSpeed

    def draw(self):
        self.image.draw(self.x,self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        #self.x, self.y = 0, 90
        self.x, self.y = random.randint(100, 700), 90
        #self.frame = 0
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()
#boy = Boy()
ballMax = 20
Balls = [Ball() for i in range(ballMax)]
team = [Boy() for i in range(11)]
grass = Grass()

running = True
# game main loop code
while running:
    handle_events()

    #boy.update()
    for boy in team:
        boy.update()
    for Ball in Balls:
        Ball.update()
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for Ball in Balls:
        Ball.draw()
    update_canvas()

    delay(0.05)
# finalization code
close_canvas()