import os; import sys; import types
import importlib.machinery
import game
import pygame
from game import *
from pygame.locals import *
from game import Game
from ui import UserInterface
from input import InputHandler
from controllers import Controller

def main():
    pygame.init()
    
    # Set up the game window
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Accessible Game")

    # Initialize game components
    game = Game()
    ui = UserInterface(screen)
    input_handler = InputHandler()
    controller = Controller()

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Handle input
            input_handler.handle_event(event)
            controller.handle_event(event)

        # Update game state
        game.update()
        
        # Render UI
        ui.render(game)

        # Refresh the screen
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()