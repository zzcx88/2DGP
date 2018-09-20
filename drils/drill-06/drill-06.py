from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
   global running
   global x, y
   global ifClick
   events = get_events()
   for event in events:
        if event.type == SDL_QUIT:
           running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
           x , y = event.x, KPU_HEIGHT - 1 - event.y
           ifClick = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
           running = False

open_canvas(KPU_WIDTH, KPU_HEIGHT)


# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse_cursor = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
ifClick = True
cx = 0
cy = 0
frame = 0
## hide_cursor()
#character.clip_draw(frame * 100, 100 * 1, 100, 100, KPU_WIDTH / 2 , KPU_HEIGHT / 2)
while running:
    while ifClick == True:
        while x != cx and y != cy:
            mouse_cursor.draw(100, 100)
            clear_canvas()
            kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
            if x - cx < 0 and y - cy < 0:
                cx -= 5
                cy -= y / (x / 5)
            if x - cx > 0 and y - cy > 0:
                cx += 5
                cy += y / (x / 5);
            if x - cx < 0 and y - cy > 0:
                cx -= 5
                cy += y / (x / 5);
            if x - cx > 0 and y - cy < 0:
                cx += 5
                cy -= y / (x / 5);
            character.clip_draw(frame * 100, 100 * 1, 100, 100, cx, cy)
            frame = (frame + 1) % 8
            update_canvas()
            delay(0.02)
            handle_events()
    ifClick = False

close_canvas()




