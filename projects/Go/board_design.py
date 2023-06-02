import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

GRID_SIZE = 30
MARGIN = 2


class GameBoard:
    def __init__(self, screen, board_size):
        self.screen = screen
        self.board_size = board_size
        self.board_color = WHITE
        self.grid_color = BLACK
        self.grid_width = 1
        self.stone_radius = int(GRID_SIZE / 2) - 2

    def draw_board(self, stones):
        self.screen.fill(self.board_color)

        for row in range(self.board_size):
            for col in range(self.board_size):
                x = MARGIN + col * GRID_SIZE
                y = MARGIN + row * GRID_SIZE
                pygame.draw.circle(self.screen, self.grid_color, (x, y), self.stone_radius, self.grid_width)

        for row in range(self.board_size):
            for col in range(self.board_size):
                x = MARGIN + col * GRID_SIZE
                y = MARGIN + row * GRID_SIZE
                stone = stones[col][row]
                if stone == BLACK:
                    stone_color = (0, 0, 0)  # Black color
                elif stone == WHITE:
                    stone_color = (255, 255, 255)  # White color
                else:
                    stone_color = (0, 0, 0)  # Default color for empty spaces
                if stone is not None:
                    pygame.draw.circle(self.screen, stone_color, (x, y), self.stone_radius)

        pygame.display.flip()
