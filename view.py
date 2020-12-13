import pygame
from pygame.locals import MOUSEBUTTONDOWN, QUIT
from settings import TITLE, CELL_SIZE, BOARD_SIZE, RESET_BUTTON_HEIGHT, \
    BACKGROUND_COLOR, MAIN_GUI_COLOR, O_COLOR, X_COLOR, WINNER_LINE_COLOR


class View:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)

        board_sizes = (BOARD_SIZE*CELL_SIZE, BOARD_SIZE*CELL_SIZE)
        screen_sizes = (board_sizes[0], board_sizes[1]+RESET_BUTTON_HEIGHT)

        self.screen = pygame.display.set_mode(screen_sizes)
        self.board = pygame.Surface(board_sizes)
        self.reset()

    def get_events(self):
        events = []
        for x in pygame.event.get():
            if x.type == QUIT:
                events.append('QUIT')
            if x.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if y > BOARD_SIZE*CELL_SIZE:
                    events.append('RESET')
                else:
                    events.append((x//CELL_SIZE, y//CELL_SIZE))
        return events

    def reset(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.board.fill(BACKGROUND_COLOR)
        for i in range(1, BOARD_SIZE):
            start_pos = (i*CELL_SIZE, 0)
            end_pos = (i*CELL_SIZE, BOARD_SIZE*CELL_SIZE)
            pygame.draw.line(self.board, MAIN_GUI_COLOR, start_pos, end_pos)

        for i in range(1, BOARD_SIZE):
            start_pos = (0, i*CELL_SIZE)
            end_pos = (BOARD_SIZE*CELL_SIZE, i*CELL_SIZE)
            pygame.draw.line(self.board, MAIN_GUI_COLOR, start_pos, end_pos)
        self.screen.blit(self.board, (0, 0))

        font = pygame.font.SysFont('Arial', RESET_BUTTON_HEIGHT - 12)
        text = font.render('RESET', True, MAIN_GUI_COLOR)
        self.screen.blit(text, (6, BOARD_SIZE*CELL_SIZE+6))

        pygame.display.flip()

    def x_move(self, x, y):
        startpos1 = (x*CELL_SIZE, y*CELL_SIZE)
        endpos1 = ((x+1)*CELL_SIZE, (y+1)*CELL_SIZE)
        startpos2 = ((x+1)*CELL_SIZE, y*CELL_SIZE)
        endpos2 = (x*CELL_SIZE, (y+1)*CELL_SIZE)

        pygame.draw.line(self.board, O_COLOR, startpos1, endpos1)
        pygame.draw.line(self.board, O_COLOR, startpos2, endpos2)
        self.screen.blit(self.board, (0, 0))
        pygame.display.flip()

    def o_move(self, x, y):
        rect = pygame.Rect(
            x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.ellipse(self.board, X_COLOR, rect, 1)
        self.screen.blit(self.board, (0, 0))
        pygame.display.flip()

    def highlight_line(self, start, end):
        a, b = start, end
        startpos = ((a[0]+0.5)*CELL_SIZE, (a[1]+0.5)*CELL_SIZE)
        endpos = ((b[0]+0.5)*CELL_SIZE, (b[1]+0.5)*CELL_SIZE)
        pygame.draw.line(self.board, WINNER_LINE_COLOR, startpos, endpos, 4)
        self.screen.blit(self.board, (0, 0))
        pygame.display.flip()
