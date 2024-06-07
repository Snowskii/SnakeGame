from commands import Commands


class Snake():

    def __init__(self):
        self.position = [100, 50]
        self.body = [
                [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
        ]
        self.direction: Commands = Commands.RIGHT

    def move_snake(self, direction) -> None:
        match direction:
            case Commands.UP:
                self.position[1] -= 10
            case Commands.DOWN:
                self.position[1] += 10
            case Commands.LEFT:
                self.position[0] -= 10
            case Commands.RIGHT:
                self.position[0] += 10
