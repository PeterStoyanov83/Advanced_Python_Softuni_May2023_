import pygame
from board_design import GameBoard
from game_over_screen import game_over_screen

# Constants for the game
BOARD_SIZE = 19
GRID_SIZE = 30
SCREEN_SIZE = (BOARD_SIZE * GRID_SIZE, BOARD_SIZE * GRID_SIZE)
PLAYER_VS_PLAYER = 1
PLAYER_VS_COMPUTER = 2


def welcome_screen(screen, SCREEN_SIZE):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    screen.fill(WHITE)  # Fill the screen with white color

    font = pygame.font.Font(None, 36)
    title_text = font.render("Go Game", True, BLACK)
    screen.blit(title_text, (SCREEN_SIZE[0] // 2 - title_text.get_width() // 2, 50))

    pvp_text = font.render("Player vs Player", True, BLACK)
    screen.blit(pvp_text, (SCREEN_SIZE[0] // 2 - pvp_text.get_width() // 2, 150))

    pvc_text = font.render("Player vs Computer", True, BLACK)
    screen.blit(pvc_text, (SCREEN_SIZE[0] // 2 - pvc_text.get_width() // 2, 200))

    pygame.display.flip()  # Update the display

    # Wait for player's selection
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if pvp_text.get_rect(topleft=(SCREEN_SIZE[0] // 2 - pvp_text.get_width() // 2, 150)).collidepoint(
                        mouse_pos
                ):
                    return PLAYER_VS_PLAYER, 0
                elif pvc_text.get_rect(topleft=(SCREEN_SIZE[0] // 2 - pvc_text.get_width() // 2, 200)).collidepoint(
                        mouse_pos
                ):
                    # Check the intelligence level selection
                    if level1_text.get_rect(
                            topleft=(SCREEN_SIZE[0] // 2 - level1_text.get_width() // 2 - 100, 450)).collidepoint(
                            mouse_pos
                    ):
                        return PLAYER_VS_COMPUTER, 1
                    elif level2_text.get_rect(
                            topleft=(SCREEN_SIZE[0] // 2 - level2_text.get_width() // 2, 450)).collidepoint(
                            mouse_pos
                    ):
                        return PLAYER_VS_COMPUTER, 2
                    elif level3_text.get_rect(
                            topleft=(SCREEN_SIZE[0] // 2 - level3_text.get_width() // 2 + 100, 450)).collidepoint(
                            mouse_pos
                    ):
                        return PLAYER_VS_COMPUTER, 3
