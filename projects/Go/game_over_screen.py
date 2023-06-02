import pygame

def game_over_screen(winner):
    # Initialize Pygame
    pygame.init()

    # Define screen size
    SCREEN_SIZE = (400, 200)

    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Game Over")

    # Fill the screen with white color
    screen.fill((255, 255, 255))

    # Create a font object
    font = pygame.font.Font(None, 36)

    # Create text based on the winner
    if winner == "B":
        text = font.render("Black player wins!", True, (0, 0, 0))
    elif winner == "W":
        text = font.render("White player wins!", True, (0, 0, 0))
    else:
        text = font.render("It's a tie!", True, (0, 0, 0))

    # Position the text in the center of the screen
    text_rect = text.get_rect(center=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2))

    # Draw the text on the screen
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

    # Wait for the user to close the window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
