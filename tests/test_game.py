from unittest.mock import Mock, patch
import pygame
from game import Game
from commands import Commands
from snake import Snake
from apple import Apple


def test_game_initialization():
    game = Game()
    assert game.window_x == 720
    assert game.window_y == 480
    assert game.snake_speed == 15
    assert game.score == 0
    assert isinstance(game.apple, Apple)
    assert isinstance(game.snake, Snake)


@patch('pygame.event.get')
def test_handle_events(mock_event_get):
    game = Game()

    # Create a list of mock events to simulate the user input
    mock_events = [
        Mock(type=pygame.KEYDOWN, key=pygame.K_UP),
        Mock(type=pygame.KEYDOWN, key=pygame.K_DOWN),
        Mock(type=pygame.KEYDOWN, key=pygame.K_LEFT),
        Mock(type=pygame.KEYDOWN, key=pygame.K_RIGHT),
        Mock(type=pygame.KEYDOWN, key=pygame.K_q),
    ]

    mock_event_get.side_effect = [[event] for event in mock_events]

    # Test UP key
    direction = Commands.RIGHT
    new_direction = game.handle_events(direction)
    assert new_direction == Commands.UP

    # Test DOWN key
    direction = Commands.RIGHT
    new_direction = game.handle_events(direction)
    assert new_direction == Commands.DOWN

    # Test LEFT key
    direction = Commands.UP
    new_direction = game.handle_events(direction)
    assert new_direction == Commands.LEFT

    # Test RIGHT key
    direction = Commands.UP
    new_direction = game.handle_events(direction)
    assert new_direction == Commands.RIGHT

    # Test QUIT key
    direction = Commands.UP
    new_direction = game.handle_events(direction)
    assert new_direction == Commands.QUIT

    # Test no direction change if moving up and pressing down
    mock_event_get.side_effect = [[Mock(type=pygame.KEYDOWN,
                                        key=pygame.K_DOWN)]]
    direction = Commands.UP
    new_direction = game.handle_events(direction)
    assert new_direction == Commands.UP

    # Test no direction change if moving down and pressing up
    mock_event_get.side_effect = [[Mock(type=pygame.KEYDOWN, key=pygame.K_UP)]]
    direction = Commands.DOWN
    new_direction = game.handle_events(direction)
    assert new_direction == Commands.DOWN

    # Test no direction change if moving left and pressing right
    mock_event_get.side_effect = [[Mock(type=pygame.KEYDOWN,
                                        key=pygame.K_RIGHT)]]
    direction = Commands.LEFT
    new_direction = game.handle_events(direction)
    assert new_direction == Commands.LEFT

    # Test no direction change if moving right and pressing left
    mock_event_get.side_effect = [[Mock(type=pygame.KEYDOWN,
                                        key=pygame.K_LEFT)]]
    direction = Commands.RIGHT
    new_direction = game.handle_events(direction)
    assert new_direction == Commands.RIGHT
