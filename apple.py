import random


class Apple:

    def __init__(self, window_x, window_y):
        self.window_x = window_x
        self.window_y = window_y
        self.position: list[int] = [random.randrange(1, window_x//10) * 10,
                                    random.randrange(1, window_y//10) * 10]
        self.spawn: bool = True

    def set_random_pos(self):
        self.position[0] = random.randrange(1, self.window_x//10) * 10
        self.position[1] = random.randrange(1, self.window_y//10) * 10
