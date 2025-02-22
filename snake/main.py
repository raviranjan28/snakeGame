#!/usr/bin/env python3

"""
Snake Game - Main Entry Point
This module initializes and starts the Snake Game.
"""

import sys
import pygame
from game.game import Game
from game.config import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    FPS
)

def main():
    # Initialize Pygame
    pygame.init()
    
    # Create the game window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)
    
    try:
        # Create game instance
        game = Game(screen)
        
        # Start the game loop
        game.run()
        
    except Exception as e:
        print(f"Error occurred: {e}", file=sys.stderr)
        return 1
    finally:
        # Clean up Pygame resources
        pygame.quit()
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 