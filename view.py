import pygame
from pygame.locals import MOUSEBUTTONDOWN, QUIT
from settings import CELL_SIZE, RESET_BUTTON_HEIGHT, TITLE, BACKGROUND_COLOR


class View:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)

        board_sizes = (3*CELL_SIZE, 3*CELL_SIZE)
        screen_sizes = (board_sizes[0], board_sizes[1]+RESET_BUTTON_HEIGHT)

        self.screen = pygame.display.set_mode(screen_sizes)
        self.board = pygame.Surface(board_sizes)
        self.screen.fill(BACKGROUND_COLOR)
        pygame.display.flip()

    def get_events(self):
        events = []
        for x in pygame.event.get():
            if x.type == QUIT:
                events.append('QUIT')
            if x.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if y > 3*CELL_SIZE:
                    events.append('RESET')
                else:
                    events.append((x//CELL_SIZE, y//CELL_SIZE))
        return events

    def reset(self):
        pass

    def x_move(self, x, y):
        pass

    def o_move(self, x, y):
        pass

    def highlight_line(start, end):
        pass
