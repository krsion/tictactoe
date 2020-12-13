import random


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
                        view.o_move(x, y)
                    player_begins = not player_begins
                elif is_game:
                    x, y = event
                    view.x_move(x, y)
                    winner_line = state.winner_line((x, y))
                    if winner_line:
                        is_game = False
                        view.highlight_line(winner_line)
                        continue
                    x, y = bot.move(state)
                    view.o_move(x, y)
                    winner_line = state.winner_line((x, y))
                    if winner_line:
                        is_game = False
                        view.highlight_line(winner_line)
                        continue
