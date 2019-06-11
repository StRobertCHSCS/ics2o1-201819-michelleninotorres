"""
1. Use a loop to generate a lot of rain.
"""
import random
import arcade


WIDTH = 640
HEIGHT = 480
FRAME_COUNT = 0
SCORE = 0

angle = 32
dead = False


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
rain_picture = arcade.load_texture("raindrop-clipart-uses-water-7.png")
dragonfly_picture =arcade.load_texture("Dragonfly-PNG-Background-Image.png")

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
   arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
   arcade.set_background_color(arcade.color.WHITE)
   arcade.schedule(update, 1 / 60)

   # Override arcade window methods
   window = arcade.get_window()
   window.on_draw = on_draw
   window.on_key_press = on_key_press
   window.on_key_release = on_key_release

   arcade.run()


def update(delta_time):
    global up_pressed, player_y, down_pressed, player_x, left_pressed, player_x, right_pressed, lives, x, y, touched, death_timer, dead
    for index in range(len(rain_y_positions)):
       rain_y_positions[index] -= 5

       if rain_y_positions[index] < 0:
           rain_y_positions[index] = random.randrange(HEIGHT, HEIGHT+50)
           rain_x_positions[index] = random.randrange(0, WIDTH)

    for i in range(0, (len(rain_x_positions))):
        distance = ((player_x - rain_x_positions[i])**2 + (player_y - rain_y_positions[i])**2)**0.5
        if distance <= 50:
            dead = True

    if dead:
        exit()



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
    global FRAME_COUNT, SCORE
    FRAME_COUNT += 10000000000
    if FRAME_COUNT % 30 == 0:
            SCORE += 1

    global angle

    if right_pressed:
        angle = angle - 3

    if left_pressed:
        angle = angle + 3


def on_draw():
   arcade.start_render()
   # Draw in here...
   arcade.draw_texture_rectangle(WIDTH/2, HEIGHT/2, 2*background.width, 2*background.height, background, 90)
   for x, y in zip(rain_x_positions, rain_y_positions):
    #arcade.draw_circle_filled(x, y, 7, arcade.color.GREEN)
       arcade.draw_texture_rectangle(x,y, 0.04*rain_picture.width, 0.04*rain_picture.height, rain_picture)
   global player_x, player_y, angle
   # Draw in here...

   arcade.draw_text(str(SCORE), 100, 100, arcade.color.BLACK, 50)


   texture = arcade.load_texture("Dragonfly-PNG-Background-Image.png")
   scale = .05
   arcade.draw_texture_rectangle(player_x, player_y, scale * texture.width,
                                 scale * texture.height, texture, angle)

   # Draw in here...


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

