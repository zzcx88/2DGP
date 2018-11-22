import random
from pico2d import *
import game_world
import game_framework

global cx, cy

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.cx, self.cy = 0, 0
        self.x, self.y, self.fall_speed = random.randint(20,1700), random.randint(0,1100), 0

    def get_bb(self):
        return self.cx - 10, self.cy - 10, self.cx + 10, self.cy + 10

    def draw(self):
         # self.image.draw(self.x, self.y)
         cx, cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
         self.cx, self.cy = cx, cy
         self.image.draw(self.cx, self.cy)
         draw_rectangle(*self.get_bb())
    def set_background(self, bg):
        self.bg = bg

    def update(self):
         self.y -= self.fall_speed * game_framework.frame_time
