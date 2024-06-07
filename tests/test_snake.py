from snake import Snake
from commands import Commands


def test_snake_initialization():
    snake = Snake()
    assert snake.position == [100, 50]
    assert snake.body == [[100, 50], [90, 50], [80, 50], [70, 50]]
    assert snake.direction == Commands.RIGHT


def test_snake_move():
    snake = Snake()
    initial_position = snake.position.copy()
    snake.move_snake(Commands.UP)
    assert snake.position == [initial_position[0], initial_position[1] - 10]
