from direction import Direction


class Snake():

    def __init__(self):
        self.position = [100, 50]
        self.body = [
                [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
        ]
        self.direction: Direction = Direction.RIGHT
