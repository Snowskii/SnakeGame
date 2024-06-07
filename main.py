import pygame
import time
import random
from score import Score


class Game():
    snake_speed: int = 15
    window_x: int = 720
    window_y: int = 480
    score: int = 0


class Color():
    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    RED = pygame.Color(255, 0, 0)
    GREEN = pygame.Color(0, 255, 0)
    BLUE = pygame.Color(0, 0, 255)


# Initialization of game
pygame.init()
pygame.display.set_caption("SnakeGame with a twist?")
game_window = pygame.display.set_mode((Game.window_x, Game.window_y))
fps = pygame.time.Clock()

snake_position = [100, 50]
snake_body = [
    [100, 50]
    [90, 50]
    [80, 50]
    [70, 50]
]

apple_position = [random.randrange(1, (Game.window_x//10)) * 10,
                  random.randrange(1, (Game.window_y//10)) * 10]
apple_spawn = True

direction = "RIGHT"
change_to = direction


def show_score(choice, color, font, size, game_window):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(Game.score), True,
                                      color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)


# game over function
def game_over():

    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(Game.score),
                                       True, Color.RED)

    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (Game.window_x/2, Game.window_y/4)

    game_window.blit(game_over_surface, game_over_rect)

    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()
