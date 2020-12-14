from settings import BOT, PLAYER, EMPTY, BOARD_SIZE, N_WINS


class State:
    def __init__(self, board=None, last_move=None):
        """ board = 2D list, last_move = tuple of coordinates (x,y) """
        self.board = board
        self.last_move = last_move
        if not board:
            self.board = [[EMPTY for _ in range(BOARD_SIZE)]
                          for _ in range(BOARD_SIZE)]

    def __str__(self):
        s = str(self.last_move) + \
            str(self.board[self.last_move[1]][self.last_move[0]]) + '\n'
        for line in self.board:
            for cell in line:
                s += str(cell)
            s += '\n'
        s += '\n'
        return s

    def update(self, x, y, who):
        self.board[y][x] = who
        self.last_move = (x, y)

    def reset(self):
        self.board = [[EMPTY for _ in range(BOARD_SIZE)]
                      for _ in range(BOARD_SIZE)]
        self.last_move = None

    def fits(self, x, y):
        """ Returns False if the coordinates aren't within the valid range """
        return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE

    def move_is_valid(self, x, y):
        """ Checks if the place is empty, not if it fits """
        return self.board[y][x] == EMPTY

    def board_is_full(self):
        """ Checks if there are some empty cells """
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

    def children(self):
        """
        Generates all possible states after this state.
        If exists, the state with last_move in the middle is put to be first.
        """
        last_player = self.board[self.last_move[1]
                                 ][self.last_move[0]] if self.last_move else None
        player = BOT if last_player == PLAYER else PLAYER
        children = []
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                if self.board[y][x] == EMPTY:
                    child = State([x[:] for x in self.board], (x, y))
                    child.board[y][x] = player
                    if x == y == 1:
                        children = [child]+children
                    else:
                        children.append(child)
        return children


class Bot:
    def move(self, state):
        # return (0, 0)
        best_state = state
        best_score = -100000
        i = 0
        for child in state.children():
            i += 1
            score = Bot.minimax(child, 4, False)

            if best_score < score:
                best_score = score
                best_state = child
        return best_state.last_move

    def minimax(state, depth, maxing):
        if depth <= 0 or state.board_is_full() or Bot.evaluate(state) > 0:
            return Bot.evaluate(state)
        children = state.children()
        if maxing:
            val = -1
            for x in children:
                val = max(val, Bot.minimax(x, depth-1, False))
            return val
        else:
            val = 1
            for x in children:
                val = min(val, Bot.minimax(x, depth-1, True))
            return val

    def evaluate(state):
        def check_for(who):
            B = state.board
            for i in range(3):
                if B[i] == [who, who, who] or B[0][i] == B[1][i] == B[2][i] == who:
                    return True
            if B[0][0] == B[1][1] == B[2][2] == who:
                return True
            return False

        if check_for(PLAYER):
            return -1
        if check_for(BOT):
            return 1
        return 0
