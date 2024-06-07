import pygame
from game import Game
from color import Color

game = Game()

# Main Function
while True:

    game.snake.direction = game.handle_events(game.snake.direction)
    game.move_snake(game.snake.direction)

    game.snake.body.insert(0, list(game.snake.position))
    if game.snake.position[0] == game.apple.position[0] and game.snake.position[1] == game.apple.position[1]:
        game.score += 1
        game.apple.spawn = False
    else:
        game.snake.body.pop()

    if not game.apple.spawn:
        game.apple.set_random_pos()

    game.apple.spawn = True
    game.window.fill(Color.BLACK)

    for pos in game.snake.body:
        pygame.draw.rect(game.window, Color.GREEN,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game.window, Color.WHITE, pygame.Rect(
        game.apple.position[0], game.apple.position[1], 10, 10))

    # Game Over conditions
    if game.snake.position[0] < 0 or game.snake.position[0] > Game.window_x-10:
        game.game_over()
    if game.snake.position[1] < 0 or game.snake.position[1] > Game.window_y-10:
        game.game_over()

    for block in game.snake.body[1:]:
        if game.snake.position[0] == block[0] and game.snake.position[1] == block[1]:
            game.game_over()

    game.show_score(Color.WHITE, 'times new roman', 20, game.window)

    pygame.display.update()

    game.fps.tick(game.snake_speed)
