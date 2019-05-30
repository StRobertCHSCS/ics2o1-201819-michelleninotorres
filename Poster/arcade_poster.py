import arcade

WIDTH = 640
HEIGHT = 480

my_button = (320, 410, 280, 40)


title_y = 500


def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    global title_x, title_delta_y, title_y



    if title_y > 400:
        title_y -= 1

    #arcade.draw_text("Fortnite addiction", 200, 400, arcade.color.BLACK, 20)
    arcade.draw_text("Fortnite addiction", 200, title_y, arcade.color.BLACK, 20)
    arcade.draw_rectangle_outline(320, title_y + 10, 280, 40, arcade.color.BLACK, 5)
    arcade.draw_text("Fortnite addiction is putting kids all around the world in video game rehab centers", 30, 350, arcade.color.BLACK, 11)
    arcade.draw_text("Fortnite is even affecting professional sports teams", 30, 320, arcade.color.BLACK, 11)
    arcade.draw_text("Such as the vancouver cancuks, they have banned all there players from playing", 30, 300, arcade.color.BLACK,11)
    arcade.draw_text("Over 200 million people have a fortnite account and I'm one of them", 30, 270, arcade.color.BLACK,11)
    arcade.draw_text("This has led to epic games being worth several billion dollars", 30, 250, arcade.color.BLACK,11)
    arcade.draw_text("And many fortnite addicts have followed", 30, 200, arcade.color.BLACK, 12)

    texture = arcade.load_texture("purepng.webp")
    scale = .1
    arcade.draw_texture_rectangle(540, 120, scale * texture.width,
                                  scale * texture.height, texture, 0)

    texture = arcade.load_texture("kisspng-computer-addiction-internet-addiction-disorder-vid-5c0fb627812874.993819791544533543529.png")
    scale = .1
    arcade.draw_texture_rectangle(100, 120, scale * texture.width,
                                  scale * texture.height, texture, 0)

    texture = arcade.load_texture("epic-games-logo.png")
    scale = .1
    arcade.draw_texture_rectangle(320, 120, scale * texture.width,
                                  scale * texture.height, texture, 0)

def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    my_button_x, my_button_y, my_button_w, my_button_h = my_button

    # Need to check all four limits of the button.
    if (x > my_button_x and x < my_button_x + my_button_w and
            y > my_button_y and y < my_button_y + my_button_h):
        website = "https://www.thestar.com/life/2018/12/02/fortnite-addiction-is-forcing-kids-into-video-game-rehab.html"



def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.BONDI_BLUE)
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
