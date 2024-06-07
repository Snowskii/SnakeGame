import pygame
import time
import random
from direction import Direction
from color import Color
from snake import Snake


class Game():
    window_x: int = 720
    window_y: int = 480

    def __init__(self):
        self.snake_speed: int = 15
        self.score: int = 0
        self.snake: Snake = Snake()

    def handle_events(self, direction: Direction) -> Direction:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != Direction.DOWN:
                    return Direction.UP
                if event.key == pygame.K_DOWN and direction != Direction.UP:
                    return Direction.DOWN
                if event.key == pygame.K_LEFT and direction != Direction.RIGHT:
                    return Direction.LEFT
                if event.key == pygame.K_RIGHT and direction != Direction.LEFT:
                    return Direction.RIGHT
                else:
                    return Direction.QUIT
        return direction


# Initialization of game
pygame.init()
pygame.display.set_caption("SnakeGame with a twist?")
game_window = pygame.display.set_mode((Game.window_x, Game.window_y))
fps = pygame.time.Clock()

game = Game()


apple_position = [random.randrange(1, (Game.window_x//10)) * 10,
                  random.randrange(1, (Game.window_y//10)) * 10]
apple_spawn = True

direction = Direction.RIGHT


def show_score(choice, color, font, size, game_window):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(game.score), True,
                                      color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)


# game over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(game.score),
                                       True, Color.RED)

    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (Game.window_x/2, Game.window_y/4)

    game_window.blit(game_over_surface, game_over_rect)

    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()


# Main Function
while True:

    direction = game.handle_events(direction)

    match direction:
        case Direction.UP:
            game.snake.position[1] -= 10
        case Direction.DOWN:
            game.snake.position[1] += 10
        case Direction.LEFT:
            game.snake.position[0] -= 10
        case Direction.RIGHT:
            game.snake.position[0] += 10
        case Direction.QUIT:
            game_over()

    game.snake.body.insert(0, list(game.snake.position))
    if game.snake.position[0] == apple_position[0] and game.snake.position[1] == apple_position[1]:
        game.score += 1
        fruit_spawn = False
    else:
        game.snake.body.pop()

    if not apple_spawn:
        apple_position = [random.randrange(1, (Game.window_x//10)) * 10,
                          random.randrange(1, (Game.window_y//10)) * 10]

    fruit_spawn = True
    game_window.fill(Color.BLACK)

    for pos in game.snake.body:
        pygame.draw.rect(game_window, Color.GREEN,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, Color.WHITE, pygame.Rect(
        apple_position[0], apple_position[1], 10, 10))

    # Game Over conditions
    if game.snake.position[0] < 0 or game.snake.position[0] > Game.window_x-10:
        game_over()
    if game.snake.position[1] < 0 or game.snake.position[1] > Game.window_y-10:
        game_over()

    for block in game.snake.body[1:]:
        if game.snake.position[0] == block[0] and game.snake.position[1] == block[1]:
            game_over()

    show_score(1, Color.WHITE, 'times new roman', 20, game_window)

    pygame.display.update()

    fps.tick(game.snake_speed)
