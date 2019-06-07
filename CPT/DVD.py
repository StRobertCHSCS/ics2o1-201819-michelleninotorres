import arcade


WIDTH = 640
HEIGHT = 480
x = 100
y = 100
z = 2.5
n = 2.5

a = 443
b = 267
c = 2.5
d = 2.5

def on_update(delta_time):
    global x
    global y
    global z
    global n
    x = x + z
    y = y + n

    global a
    global b
    global c
    global d

    a = a + c
    b = b + d

    if x > 590 or x < 50:
        z = z * -1
    if y > 450 or y < 30:
        n = n * -1

    if a > 590 or a < 50:
        c = c * -1
    if b > 450 or b < 30:
        d = d * -1

    if a == x:
        c = c *-1
    if a == x:
        n = n *-1

    if y == b:
        d = d*-1

    if y == b:
        z = z * -1


def on_draw():
    arcade.start_render()
    # Draw in here...
    arcade.draw_circle_filled(x, y, 55, arcade.color.WHITE)

    texture = arcade.load_texture("Computer-Hardware-Dvd-icon.png")
    scale = .2
    arcade.draw_texture_rectangle(x, y, scale * texture.width, scale * texture.height, texture, 0)

    texture = arcade.load_texture("Blu_ray_logo.png")
    scale = .05
    arcade.draw_texture_rectangle(a, b ,scale * texture.width, scale * texture.height, texture, 0)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
