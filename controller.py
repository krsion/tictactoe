import random
from settings import PLAYER, BOT


class Controller:
    def __init__(self, state, bot, view):
        is_running = True
        is_game = True
        player_begins = True
        while is_running:
            for event in view.get_events():
                if event == 'QUIT':
                    is_running = False
                elif event == 'RESET':
                    is_game = True
                    view.reset()
                    state.reset()
                    if player_begins:
                        x, y = bot.move(state)
                        state.update(x, y, BOT)
                        view.o_move(x, y)
                    player_begins = not player_begins
                elif is_game:
                    x, y = event
                    if not state.move_is_valid(x, y):
                        break  # out of the for cycle through events
                    view.x_move(x, y)
                    state.update(x, y, PLAYER)
                    winner_line = state.winner_line((x, y))
                    if winner_line or state.board_is_full():
                        is_game = False
                        if winner_line:
                            view.highlight_line(*winner_line)
                        continue

                    x, y = bot.move(state)
                    # if not state.move_is_valid(x, y):     probably not necessary
                    #    continue
                    view.o_move(x, y)
                    state.update(x, y, BOT)
                    winner_line = state.winner_line((x, y))
                    if winner_line or state.board_is_full():
                        is_game = False
                        if winner_line:
                            view.highlight_line(*winner_line)
                        continue
