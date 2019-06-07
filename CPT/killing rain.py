"""
1. Use a loop to generate a lot of rain.
"""
import random
import arcade


WIDTH = 640
HEIGHT = 480
#player x = original position on x
#player_y = original position on y
# start player position in middle of window
player_x = WIDTH/2
player_y = HEIGHT/2

# Variables to record if certain keys are being pressed.
up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False

rain = arcade.ShapeElementList()
background = arcade.load_texture("f948f6f5453a26689f0a6d63294e9b74.jpg")

# first set up empty lists
rain_x_positions = []
rain_y_positions = []

# loop 100 times
for _ in range(10):
   # generate random x and y values
   x = random.randrange(0, WIDTH)
   y = random.randrange(HEIGHT, HEIGHT*2)

   # append the x and y values to the appropriate list
   rain_x_positions.append(x)
   rain_y_positions.append(y)


def setup():
   arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
   arcade.set_background_color(arcade.color.WHITE)
   arcade.schedule(update, 1/60)

   # Override arcade window methods
   window = arcade.get_window()
   window.on_draw = on_draw
   window.on_key_press = on_key_press
   window.on_key_release = on_key_release
   window.on_mouse_press = on_mouse_press

   arcade.run()


def update(delta_time):
    global up_pressed, player_y, down_pressed, player_x, left_pressed, player_x, right_pressed
    for index in range(len(rain_y_positions)):
       rain_y_positions[index] -= 5

       if rain_y_positions[index] < 0:
           rain_y_positions[index] = random.randrange(HEIGHT, HEIGHT+50)
           rain_x_positions[index] = random.randrange(0, WIDTH)


    if up_pressed:
        player_y += 5
    global down_pressed
    if down_pressed:
        player_y -= 5
    global left_pressed
    if left_pressed:
        player_x -= 5
    global right_pressed
    if right_pressed:
        player_x += 5

def on_draw():
   arcade.start_render()
   # Draw in here...
   arcade.draw_texture_rectangle(WIDTH/2, HEIGHT/2, 2*background.width, 2*background.height, background, 90)
   for x, y in zip(rain_x_positions, rain_y_positions):
       arcade.draw_circle_filled(x, y, 7, arcade.color.GREEN)
   global player_x, player_y
   # Draw in here...
   arcade.draw_circle_filled(player_x, player_y, 15, arcade.color.BLUE)


def on_key_press(key, modifiers):
        global up_pressed
        if key == arcade.key.W:
            up_pressed = True
        global down_pressed
        if key == arcade.key.S:
            down_pressed = True
        global left_pressed
        if key == arcade.key.A:
            left_pressed = True
        global right_pressed
        if key == arcade.key.D:
            right_pressed = True


def on_key_release(key, modifiers):
    global up_pressed
    if key == arcade.key.W:
        up_pressed = False
    global down_pressed
    if key == arcade.key.S:
        down_pressed = False
    global left_pressed
    if key == arcade.key.A:
        left_pressed = False
    global right_pressed
    if key == arcade.key.D:
        right_pressed = False


def on_mouse_press(x, y, button, modifiers):
   pass


if __name__ == '__main__':
   setup()

