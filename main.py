import pygame
import time
import random

snake_speed = 15

window_x = 720
window_y = 480


class Color():
    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    RED = pygame.Color(255, 0, 0)
    GREEN = pygame.Color(0, 255, 0)
    BLUE = pygame.Color(0, 0, 255)

# Initialization of game
pygame.init()
pygame.display.set_caption("SnakeGame with a twist?")
game_window = pygame.display.set_mode((window_x, window_y))

