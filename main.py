import turtle
import time
import snake
import food
import scoreboard

SCREEN_SIZE_XY_PX = 600
BACKGROUND_COLOR = "black"
SNAKE_BODY_SHAPE = "square"
SNAKE_BODY_ELEMENT_SIZE_PX = 20
SNAKE_NR_OF_BODY_ELEMENTS = 3
SNAKE_BODY_COLOR = "white"
FOOD_COLOR = "magenta"
SCOREBOARD_COLOR = "white"


def create_snake_screen(background_color, size_px):
    screen = turtle.Screen()
    screen.setup(width=size_px, height=size_px)
    screen.bgcolor(background_color)
    screen.title("Snake")
    screen.tracer(0)  # Turns Animation off
    return screen


def initialize_controls():
    snake_screen.listen()
    snake_screen.onkey(a_snake.change_heading_left, "Left")
    snake_screen.onkey(a_snake.change_heading_right, "Right")
    snake_screen.onkey(a_snake.change_heading_up, "Up")
    snake_screen.onkey(a_snake.change_heading_down, "Down")


def collision_with_wall():
    xy_limit = SCREEN_SIZE_XY_PX / 2
    if abs(a_snake.head.xcor()) >= xy_limit:
        return True
    elif abs(a_snake.head.ycor()) >= xy_limit:
        return True
    return False


def food_caught():
    if a_snake.head.distance(food) < food.food_size:
        return True
    return False


def snake_collision_detected():
    body_segments = a_snake.body[1:]
    for segment in body_segments:
        # Round needed because function returns float that sometimes is snake.get_body_size-dxy (for example 19.999)
        if round(a_snake.head.distance(segment)) < a_snake.get_body_size():
            return True
    return False


if __name__ == '__main__':
    snake_screen = create_snake_screen(background_color=BACKGROUND_COLOR, size_px=SCREEN_SIZE_XY_PX)
    a_snake = snake.Snake(nr_of_body_elements=SNAKE_NR_OF_BODY_ELEMENTS, shape=SNAKE_BODY_SHAPE,
                        body_element_size_px=SNAKE_BODY_ELEMENT_SIZE_PX, body_color=SNAKE_BODY_COLOR)
    food = food.Food(grid_step_px=a_snake.get_body_size(), window_size_px=SCREEN_SIZE_XY_PX, color=FOOD_COLOR)
    scoreboard = scoreboard.Scoreboard(color=SCOREBOARD_COLOR)
    initialize_controls()
    game_is_on = True
    grow_snake_next_update = False
    while game_is_on:
        snake_screen.update()
        if grow_snake_next_update is True:
            a_snake.add_body_element_to_tail(shape=SNAKE_BODY_SHAPE, tail_color=SNAKE_BODY_COLOR,
                                           tail_element_size_px=SNAKE_BODY_ELEMENT_SIZE_PX)
            grow_snake_next_update = False
        scoreboard.update()
        time.sleep(0.075)
        a_snake.move()

        if collision_with_wall():
            scoreboard.update_highscore()
            scoreboard.reset_score()
            scoreboard.update()
            a_snake.reset()

        elif snake_collision_detected():
            scoreboard.update_highscore()
            scoreboard.reset_score()
            scoreboard.update()
            a_snake.reset()
        elif food_caught():
            scoreboard.increase_score()
            food.refresh_random_coordinate()
            grow_snake_next_update = True

    snake_screen.update()  # Necessary because latest Screen-Image looks like Snake did not collide with wall!
    snake_screen.exitonclick()
