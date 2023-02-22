import turtle


class Snake:
    DEFAULT_BODY_ELEMENT_SIZE_PX = 20
    body_size = DEFAULT_BODY_ELEMENT_SIZE_PX
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0

    def __init__(self, nr_of_body_elements, shape, body_element_size_px, body_color):
        self.default_nr_of_body_elements = nr_of_body_elements
        self.default_shape = shape
        self.default_body_element_size_px = body_element_size_px
        self.default_body_color = body_color
        self.body = []
        self.create_default_body()
        self.step_size = None
        self.set_step_size()
        self.head = self.body[0]
        self.tail = self.body[len(self.body) - 1]
        self.visible = True

    def create_default_body(self):
        for index in range(self.default_nr_of_body_elements):  # Create Snake
            body_element = turtle.Turtle(self.default_shape)
            body_element.penup()
            body_element.color(self.default_body_color)
            self.set_body_size(self.default_body_element_size_px, body_element)
            body_element.setposition(x=-self.default_body_element_size_px * index, y=0)
            self.body.append(body_element)

    def set_body_size(self, bdy_element_size_px, bdy_element):
        factor_x, factor_y, factor_outline = self.get_stretch_factors(size_px=bdy_element_size_px)
        bdy_element.turtlesize(factor_x, factor_y, factor_outline)
        self.body_size = bdy_element_size_px

    def get_body_size(self):
        """Returns the body size in px. Size of every body element is the same
        Note that body size is the Rect-Size (X-Y) of every body element in px"""

        stretch_factor_xy = (self.body[0].shapesize())[0]
        bdy_size = self.DEFAULT_BODY_ELEMENT_SIZE_PX * stretch_factor_xy
        return bdy_size

    def get_stretch_factors(self, size_px):
        stretch_factor_x = size_px / self.DEFAULT_BODY_ELEMENT_SIZE_PX
        stretch_factor_y = size_px / self.DEFAULT_BODY_ELEMENT_SIZE_PX
        stretch_factor_outline = 1.0
        return stretch_factor_x, stretch_factor_y, stretch_factor_outline

    def set_step_size(self):
        self.step_size = self.body_size

    def move(self):
        self.pull_body()
        self.move_head()

    def pull_body(self):
        for body_element in range(len(self.body) - 1, 0, -1):
            if body_element != 0:  # All except head
                new_x = self.body[body_element - 1].xcor()
                new_y = self.body[body_element - 1].ycor()
                self.body[body_element].goto(new_x, new_y)

    def move_head(self):
        self.head.forward(self.step_size)

    def change_heading_left(self):
        if self.head.heading() != self.RIGHT:
            self.head.setheading(self.LEFT)

    def change_heading_right(self):
        if self.head.heading() != self.LEFT:
            self.head.setheading(self.RIGHT)

    def change_heading_down(self):
        if self.head.heading() != self.UP:
            self.head.setheading(self.DOWN)

    def change_heading_up(self):
        if self.head.heading() != self.DOWN:
            self.head.setheading(self.UP)

    def get_latest_tail_coordinates(self):
        self.tail = self.body[len(self.body) - 1]
        tail_x_pos = self.tail.xcor()
        tail_y_pos = self.tail.ycor()
        return tail_x_pos, tail_y_pos

    def add_body_element_to_tail(self, shape, tail_color, tail_element_size_px):
        latest_tail_x_cor, latest_tail_y_cor = self.get_latest_tail_coordinates()
        new_tail_element = turtle.Turtle(shape)
        new_tail_element.penup()
        new_tail_element.color(tail_color)
        self.set_body_size(tail_element_size_px, new_tail_element)
        new_tail_element.setposition(x=latest_tail_x_cor, y=latest_tail_y_cor)
        self.body.append(new_tail_element)

    def reset(self):
        for element in self.body:  # Makes sure turtles of old snake are not visible anymore
            element.reset()
        self.body.clear()  # Delete old snake
        self.create_default_body()
        self.head = self.body[0]
        self.tail = self.body[len(self.body) - 1]

    def toggle_visibility(self, ):
        if self.visible:
            self.hide_body()
            self.visible = False
        else:
            self.show_body()
            self.visible = True

    def hide_body(self):
        for element in self.body:
            element.hideturtle()
    def show_body(self):
        for element in self.body:
            element.showturtle()
