class State:
    def __init__(self):
        pass

    def reset(self):
        pass

    def winner_line(self, last_move):
        pass

    def move_is_valid(self, x, y):
        return True

    def board_is_full(self):
        return False


class Bot:
    def move(self, state):
        return (0, 0)
