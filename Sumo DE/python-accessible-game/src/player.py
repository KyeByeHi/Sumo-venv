import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Define player positions
player_positions = [(100, 100), (200, 100), (300, 100), (400, 100)]

# Define player colors
player_colors = [
    (28, 231, 235),  # Player R
    (101, 214, 111),  # Player M
    (163, 88, 161),  # Player N
    (199, 0, 0)      # Player K
]

# Draw each player
for pos, color in zip(player_positions, player_colors):
    pygame.draw.circle(screen, color, pos, 20)  # Using radius 20 for better visibility

# Update the display
pygame.display.flip()

# Run a simple event loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
