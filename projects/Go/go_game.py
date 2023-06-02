import pygame
from board_design import GameBoard
from welcome_screen import welcome_screen
from game_over_screen import game_over_screen

# Constants for the game
BOARD_SIZE = 19
GRID_SIZE = 30
SCREEN_SIZE = (BOARD_SIZE * GRID_SIZE, BOARD_SIZE * GRID_SIZE)
PLAYER_VS_PLAYER = 1
PLAYER_VS_COMPUTER = 2


def handle_player_move(stones, current_player):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
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
                    return


def get_neighbors(x, y):
    neighbors = [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1)
    ]
    return [(x, y) for x, y in neighbors if is_valid_coordinate(x, y)]


def is_valid_coordinate(x, y):
    return x >= 0 and x < BOARD_SIZE and y >= 0 and y < BOARD_SIZE


def play_game():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Go Game")
    game_board = GameBoard(screen, GRID_SIZE)

    stones = [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    current_player = "B"

    black_stones_limit = 180
    white_stones_limit = 180
    black_prisoners = 0
    white_prisoners = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_board.draw_board(stones)

        handle_player_move(stones, current_player)

        # Check for captured stones and update statistics
        black_captured = 0
        white_captured = 0

        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if stones[i][j] == "":
                    neighbors = get_neighbors(i, j)
                    neighbor_colors = [stones[x][y] for x, y in neighbors if is_valid_coordinate(x, y)]
                    if "B" in neighbor_colors and "W" not in neighbor_colors:
                        black_captured += 1
                    elif "W" in neighbor_colors and "B" not in neighbor_colors:
                        white_captured += 1

        black_prisoners += black_captured
        white_prisoners += white_captured

        # Check if any player reached the stone limit
        if black_stones_limit <= 0 and white_stones_limit <= 0:
            if black_prisoners < white_prisoners:
                game_over_screen("B")  # Show game over screen with Black player as winner
            elif white_prisoners < black_prisoners:
                game_over_screen("W")  # Show game over screen with White player as winner
            else:
                game_over_screen("")  # Show game over screen as a tie

            running = False

        # Switch players
        current_player = "W" if current_player == "B" else "B"

        pygame.display.flip()

    pygame.quit()


def main():
    pygame.init()

    SCREEN_SIZE = (400, 300)
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Go Game")

    mode, intelligence_level = welcome_screen(screen, SCREEN_SIZE)
    if mode == PLAYER_VS_PLAYER:
        play_game()
    elif mode == PLAYER_VS_COMPUTER:
        # Add logic for Player vs. Computer mode
        pass

    pygame.quit()


if __name__ == "__main__":
    main()
