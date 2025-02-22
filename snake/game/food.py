"""
Food Class Module
Handles the food item's position and rendering in the game.
"""

import random
import pygame
from .config import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    BLOCK_SIZE,
    FOOD_COLOR
)

class Food:
    def __init__(self):
        """Initialize food with random position and load assets."""
        # Initialize position attributes
        self.x = 0
        self.y = 0
        
        # Calculate grid dimensions
        self.grid_width = WINDOW_WIDTH // BLOCK_SIZE
        self.grid_height = WINDOW_HEIGHT // BLOCK_SIZE
        
        # Try to load food image, fall back to rectangle if not available
        try:
            self.image = pygame.image.load("assets/images/food.png")
            self.image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE))
            self.use_image = True
        except (pygame.error, FileNotFoundError):
            self.use_image = False
        
        # Set initial random position
        self.respawn()

    def respawn(self):
        """Randomly reposition food on the game grid."""
        # Generate random grid coordinates
        grid_x = random.randint(0, self.grid_width - 1)
        grid_y = random.randint(0, self.grid_height - 1)
        
        # Convert to pixel coordinates
        self.x = grid_x * BLOCK_SIZE
        self.y = grid_y * BLOCK_SIZE

    def draw(self, screen):
        """Render the food on the screen."""
        if self.use_image:
            # Draw food using loaded image
            screen.blit(self.image, (self.x, self.y))
        else:
            # Draw food as a colored rectangle
            pygame.draw.rect(
                screen,
                FOOD_COLOR,
                pygame.Rect(
                    self.x,
                    self.y,
                    BLOCK_SIZE,
                    BLOCK_SIZE
                )
            ) 