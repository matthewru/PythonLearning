import arcade
import os
import math

SPRITE_SCALING = 1
SPRITE_SCALING_PLAYER = 0.2
SPRITE_SCALING_LASER = 0.2
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "TorpedoGame"

BULLET_SPEED = 5

window = None
class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        self.wall_list = None
        self.player_list = None
        self.bullet_list = None
        #self.background = None

        self.player_sprite = None


    def setup(self):
        self.wall_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        #Game.background = arcade.load_texture("images/sea.png", SPRITE_SCALING)

        #Left Panel
        wall = arcade.Sprite("images/TorpedoGameLeftPanel.png", SPRITE_SCALING)
        wall.center_x = 184
        wall.center_y = 500
        self.wall_list.append(wall)

        #Right Panel
        wall = arcade.Sprite("images/TorpedoGameRightPanel.png", SPRITE_SCALING)
        wall.center_x = 1616
        wall.center_y = 500
        self.wall_list.append(wall)

        self.player_sprite = arcade.Sprite("images/Battleship.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 900
        self.player_sprite.center_y = 100
        self.player_list.append

    def on_draw(self):

        arcade.start_render()

        self.wall_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):

        bullet = arcade.Sprite("images/Torpedo.png", SPRITE_SCALING_LASER)

        start_x = self.player_sprite.center_x
        start_y = self.player_sprite.center_y
        bullet.center_x = start_x
        bullet.center_y = start_y

        dest_x = x
        dest_y = y

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        bullet.angle = math.degrees(angle)
        print(f"Bullet angle: {bullet.angle:.2f}")

        bullet.change_x = math.cos(angle) * BULLET_SPEED
        bullet.change_y = math.sin(angle) * BULLET_SPEED

        self.bullet_list.append(bullet)

    #def update(self, delta_time):

        #self.bullet_list.update()


def main():
    """ Main method """
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()