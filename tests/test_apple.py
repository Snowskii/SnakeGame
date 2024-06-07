from apple import Apple


def test_apple_initialization():
    apple = Apple(720, 480)
    assert 0 <= apple.position[0] < 720
    assert 0 <= apple.position[1] < 480


def test_set_random_pos():
    apple = Apple(720, 480)
    initial_position = apple.position.copy()
    apple.set_random_pos()
    assert apple.position != initial_position
