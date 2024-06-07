import pygame
import time
from direction import Direction
from color import Color
from snake import Snake
from apple import Apple


class Game:
    window_x: int = 720
    window_y: int = 480

    def __init__(self):
        self.snake_speed: int = 15
        self.score: int = 0
        self.apple: Apple = Apple(self.window_x, self.window_y)
        self.snake: Snake = Snake()
        pygame.init()
        pygame.display.set_caption("SnakeGame with a twist?")
        self.window = pygame.display.set_mode((self.window_x, self.window_y))
        self.fps = pygame.time.Clock()

    def game_over(self) -> None:
        my_font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = my_font.render('Your Score is : ' +
                                           str(self.score), True, Color.RED)

        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (Game.window_x/2, Game.window_y/4)

        self.window.blit(game_over_surface, game_over_rect)

        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        quit()

    def show_score(self, color, font, size, game_window):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(self.score), True,
                                          color)
        score_rect = score_surface.get_rect()
        game_window.blit(score_surface, score_rect)

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
                if event.key == pygame.K_q:
                    return Direction.QUIT
        return direction

    def move_snake(self, direction) -> None:
        match direction:
            case Direction.UP:
                self.snake.position[1] -= 10
            case Direction.DOWN:
                self.snake.position[1] += 10
            case Direction.LEFT:
                self.snake.position[0] -= 10
            case Direction.RIGHT:
                self.snake.position[0] += 10
            case Direction.QUIT:
                self.game_over()
