import pygame


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (139, 69, 19)


class GameBoard:
    def __init__(self, screen, board_size):
        self.screen = screen
        self.board_size = board_size
        self.grid_size = screen.get_width() // (board_size + 2)

    def draw_board(self, stones):
        self.screen.fill(BROWN)

        for row in range(self.board_size):
            for col in range(self.board_size):
                x = (col + 1) * self.grid_size
                y = (row + 1) * self.grid_size
                pygame.draw.rect(self.screen, BLACK, (x, y, self.grid_size, self.grid_size), 1)

        pygame.display.flip()


def play_game():
    # Constants for the game
    BOARD_SIZE = 19
    GRID_SIZE = 30
    SCREEN_SIZE = (BOARD_SIZE * GRID_SIZE, BOARD_SIZE * GRID_SIZE)

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Go Game")

    game_board = GameBoard(screen, BOARD_SIZE)

    stones = [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    current_player = "B"

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_board.draw_board(stones)

        # Handle player move
        mouse_pos = pygame.mouse.get_pos()
        x = mouse_pos[0] // GRID_SIZE
        y = mouse_pos[1] // GRID_SIZE

        if (
            x >= 0
            and x < BOARD_SIZE
            and y >= 0
            and y < BOARD_SIZE
            and stones[x][y] == ""
        ):
            stones[x][y] = current_player
            current_player = "W" if current_player == "B" else "B"

        pygame.display.flip()

    pygame.quit()


def main():
    pygame.init()

    SCREEN_SIZE = (400, 300)
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Go Game")

    play_game()

    pygame.quit()


if __name__ == "__main__":
    main()
