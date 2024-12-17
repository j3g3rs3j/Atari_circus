import arcade


class Player(arcade.Sprite):
    """
    The player
    """

    def __init__(self, min_x_pos, max_x_pos, center_x=0, center_y=0, scale=1):
        """
        Setup new Player object
        """

        # Limits on player's x position
        self.min_x_pos = min_x_pos
        self.max_x_pos = max_x_pos

        # Pass arguments to class arcade.Sprite
        super().__init__(
            center_x=center_x,
            center_y=center_y,
            filename="images/playerShip1_red.png",
            scale=scale,
        )

    def on_update(self, delta_time):
        """
        Move the sprite
        """

        # Update player's x position based on current speed in x dimension
        self.center_x += delta_time * self.change_x

        # Enforce limits on player's x position
        if self.left < self.min_x_pos:
            self.left = self.min_x_pos
        elif self.right > self.max_x_pos:
            self.right = self.max_x_pos


class Acrobat(arcade.Sprite):
    """
    A shot fired by the Player
    """

    def __init__(self, center_x, center_y, max_y_pos, speed=4, scale=1, start_angle=90):
        """
        Setup new PlayerShot object
        """

        # Set the graphics to use for the sprite
        # We need to flip it so it matches the mathematical angle/direction
        super().__init__(
            center_x=center_x,
            center_y=center_y,
            scale=scale,
            filename="images/Power-ups/powerupRed_star.png",
            flipped_diagonally=True,
            flipped_horizontally=True,
            flipped_vertically=False,
        )

        # The shoot will be removed when it is above this y position
        self.max_y_pos = max_y_pos

        # Shoot points in this direction
        self.angle = start_angle

    def on_update(self, delta_time):
        """
        Move the sprite
        """

        # Remove shot when over top of screen
        if self.bottom > self.max_y_pos:
            self.kill()

class Balloons(arcade.Sprite):
    def __init__(self, center_x, center_y, screen_width, angle, row, scale=1, physics_engine=arcade.pymunk_physics_engine):
        """
        Setup new PlayerShot object
        """

        self.costume_list = ["images/Power-ups/powerupBlue.png", "images/Power-ups/powerupRed.png","images/Power-ups/powerupGreen.png"]

        # Set the graphics to use for the sprite
        super().__init__(
            center_x=center_x,
            center_y=center_y,
            scale=scale,
            filename=self.costume_list[row],
            flipped_diagonally=True,
            flipped_horizontally=True,
            flipped_vertically=False,
        )
        self.angle = angle

        self.screen_width = screen_width

        self.physics_engine = physics_engine

    def update(self):

        if self.center_x > self.screen_width + 13:
            self.physics_engine.set_position(self, (-13, self.center_y))
        if self.center_x < -13:
            self.physics_engine.set_position(self, (self.screen_width - 13, self.center_y))

    def balloon_death_sequence(self):



        self.kill()

