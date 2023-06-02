import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (139, 69, 19)


class GameBoard:
    def __init__(self, screen, board_size):
        self.screen = screen
        self.board_size = board_size
        self.grid_size = screen.get_width() // (board_size + 2)  # Calculate grid size based on screen width

    def draw_board(self, stones):
        self.screen.fill(BROWN)

        for row in range(self.board_size):
            for col in range(self.board_size):
                x = (col + 1) * self.grid_size
                y = (row + 1) * self.grid_size
                pygame.draw.rect(self.screen, BLACK, (x, y, self.grid_size, self.grid_size), 1)

        pygame.display.flip()
