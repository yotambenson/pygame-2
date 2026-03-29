import pygame
import sys
import random

# 1. Initialize Pygame
pygame.init()

# 2. Define colors (RGB tuples)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 3. Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bouncing Color Rectangle with Text")

# 4. Set up the bouncing rectangle
rect_width = 50
rect_height = 50
# Create a Rect object for easy manipulation of position and collision
bouncing_rect = pygame.Rect(
    SCREEN_WIDTH // 2 - rect_width // 2,
    SCREEN_HEIGHT // 2 - rect_height // 2,
    rect_width,
    rect_height
)
rect_color = RED
# Set initial movement speed and direction
speed_x = 5
speed_y = 5

# 5. Set up the text element
font = pygame.font.SysFont(None, 36)

# 6. Set up the game clock to control frame rate
clock = pygame.time.Clock()
FPS = 60

# 7. Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Change color on mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Generate a new random color
            rect_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # 8. Game logic (bouncing movement)
    bouncing_rect.x += speed_x
    bouncing_rect.y += speed_y

    # Check for collisions with screen boundaries
    if bouncing_rect.left < 0 or bouncing_rect.right > SCREEN_WIDTH:
        speed_x = -speed_x  # Reverse horizontal direction
    if bouncing_rect.top < 0 or bouncing_rect.bottom > SCREEN_HEIGHT:
        speed_y = -speed_y  # Reverse vertical direction

    # 9. Drawing
    screen.fill(BLACK) # Clear screen with background color each frame

    # Draw the bouncing rectangle with the current color
    pygame.draw.rect(screen, rect_color, bouncing_rect)

    # Render and blit the text
    text_surface = font.render("Click mouse to change color", True, WHITE)
    # Center the text at the top of the screen
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, 30))
    screen.blit(text_surface, text_rect)

    # 10. Update the display
    pygame.display.flip() # Update the full display Surface to the screen

    # 11. Cap the frame rate
    clock.tick(FPS)

# Quit Pygame and exit the program
pygame.quit()
sys.exit()
