import turtle
import random


class Food(turtle.Turtle):
    DEFAULT_FOOD_SIZE_PX = 20

    def __init__(self, grid_step_px, window_size_px, color):
        super().__init__()
        self.grid_step_px = grid_step_px
        self.food_coordinate_limit = window_size_px / 2 - self.grid_step_px
        self.food_size = grid_step_px / 2
        self.set_food_size()
        self.shape("circle")
        self.penup()
        self.color(color)
        self.speed("fastest")
        self.random_x_coordinate = None
        self.random_y_coordinate = None
        self.refresh_random_coordinate()

    def get_random_coordinate(self):
        self.random_x_coordinate = random.randrange(0, self.food_coordinate_limit, self.grid_step_px)\
                                   * random.choice([-1, 1])
        self.random_y_coordinate = random.randrange(0, self.food_coordinate_limit, self.grid_step_px)\
                                   * random.choice([-1, 1])

    def refresh_random_coordinate(self):
        self.get_random_coordinate()
        self.setposition(self.random_x_coordinate, self.random_y_coordinate)

    def set_food_size(self):
        factor_x, factor_y, factor_outline = self.get_stretch_factors()
        self.shapesize(factor_x, factor_y, factor_outline)

    def get_stretch_factors(self):
        stretch_factor_x = self.food_size / self.DEFAULT_FOOD_SIZE_PX
        stretch_factor_y = self.food_size / self.DEFAULT_FOOD_SIZE_PX
        stretch_factor_outline = 1.0
        return stretch_factor_x, stretch_factor_y, stretch_factor_outline
