from settings import BOT, PLAYER, EMPTY, BOARD_SIZE, N_WINS


class State:
    def __init__(self):
        self.reset()

    def update(self, x, y, who):
        self.board[y][x] = who

    def reset(self):
        self.board = [[EMPTY for _ in range(BOARD_SIZE)]
                      for _ in range(BOARD_SIZE)]

    def fits(self, x, y):
        return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE

    def move_is_valid(self, x, y):
        return self.board[y][x] == EMPTY

    def board_is_full(self):
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                if self.board[y][x] == EMPTY:
                    return False
        return True

    def winner_line(self, last_move):
        mask = [(0, 1), (1, 0), (1, 1), (1, -1)]
        x, y = last_move
        who = self.board[y][x]
        lines = [[], [], [], []]
        for i in range(-N_WINS+1, N_WINS):
            for j in range(4):
                P = (x+i*mask[j][0], y+i*mask[j][1])
                if self.fits(P[0], P[1]) and self.board[P[1]][P[0]] == who:
                    lines[j].append(P)
                    if len(lines[j]) == N_WINS:
                        return [lines[j][0], lines[j][-1]]
                else:
                    lines[j] = []


class Bot:
    def move(self, state):
        return (0, 0)
