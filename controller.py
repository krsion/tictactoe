import random
from settings import PLAYER, BOT, X_WHO, O_WHO


def update(x, y, who, state, view):
    """ Updates both state and view """
    state.update(x, y, who)
    view_update = {X_WHO: view.x_move, O_WHO: view.o_move}
    view_update[who](x, y)


def is_end(x, y, state, view):
    """ Tells if it is end of a game. If there is a winner, it marks him. """
    winner_line = state.winner_line((x, y))
    if winner_line or state.board_is_full():
        if winner_line:
            view.highlight_line(*winner_line)
        return True
    return False


def controller(state, bot, view):
    """ Here is the main logic of the game """
    is_running = True
    is_game = True
    player_begins = True
    while is_running:
        for event in view.get_events():
            if event == 'QUIT':
                is_running = False
            elif event == 'RESET':
                player_begins = not player_begins
                is_game = True
                view.reset()
                state.reset()
                if not player_begins:
                    x, y = bot.move(state)
                    update(x, y, BOT, state, view)

            elif is_game:
                x, y = event
                if not state.move_is_valid(x, y):
                    break
                update(x, y, PLAYER, state, view)
                if is_end(x, y, state, view):
                    is_game = False
                    continue

                x, y = bot.move(state)
                update(x, y, BOT, state, view)
                if is_end(x, y, state, view):
                    is_game = False
                    continue
