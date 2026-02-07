import pytest
from game.snake import Snake

def test_snake_initialization():
    snake = Snake((10, 10))
    # Default length is 3, so head (10,10), body (10,9), body (10,8) assuming direction (0,1)
    assert len(snake.body) == 3
    assert snake.body[0] == (10, 10)

def test_snake_movement():
    snake = Snake((10, 10), direction=(0, 1))
    new_head = snake.move()
    assert new_head == (10, 11)
    assert snake.body[0] == (10, 11)
    assert len(snake.body) == 3

def test_snake_growth():
    snake = Snake((10, 10), direction=(0, 1))
    snake.grow()
    snake.move()
    assert len(snake.body) == 4

def test_snake_direction_change():
    snake = Snake((10, 10), direction=(0, 1))
    snake.change_direction((1, 0)) # Turn down
    assert snake.direction == (1, 0)
    new_head = snake.move()
    assert new_head == (11, 10)

def test_snake_growth_multiple():
    snake = Snake((10, 10), direction=(0, 1))
    snake.grow(3)
    snake.move() # 1
    assert len(snake.body) == 4
    snake.move() # 2
    assert len(snake.body) == 5
    snake.move() # 3
    assert len(snake.body) == 6
    snake.move() # 4 - back to normal
    assert len(snake.body) == 6

def test_snake_prevent_reverse():
    snake = Snake((10, 10), direction=(0, 1)) # Moving right
    snake.change_direction((0, -1)) # Try to move left
    assert snake.direction == (0, 1) # Should still be moving right
