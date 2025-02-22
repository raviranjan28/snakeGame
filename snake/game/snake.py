"""
Snake Class Module
Handles the snake's movement, growth, collision detection, and rendering.
"""

import pygame
from .config import (
    BLOCK_SIZE,
    INITIAL_SNAKE_LENGTH,
    SNAKE_COLOR,
    SNAKE_HEAD_COLOR,
    INITIAL_POSITION_X,
    INITIAL_POSITION_Y,
    MOVEMENT_SPEED,
    WINDOW_WIDTH,
    WINDOW_HEIGHT
)

class Snake:
    def __init__(self):
        """Initialize the snake with starting position and segments."""
        # Starting position
        self.x = INITIAL_POSITION_X
        self.y = INITIAL_POSITION_Y
        
        # Initialize direction (snake starts moving right)
        self.direction = 'RIGHT'
        
        # Create initial snake segments
        self.segments = []
        for i in range(INITIAL_SNAKE_LENGTH):
            self.segments.append({
                'x': self.x - (i * BLOCK_SIZE),
                'y': self.y
            })
    
    def change_direction(self, new_direction):
        """
        Change the snake's direction while preventing 180-degree turns.
        """
        opposite_directions = {
            'UP': 'DOWN',
            'DOWN': 'UP',
            'LEFT': 'RIGHT',
            'RIGHT': 'LEFT'
        }
        
        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction

    def move(self):
        """Update the position of the snake's head and body segments."""
        # Calculate new head position
        new_head = {'x': self.segments[0]['x'], 'y': self.segments[0]['y']}
        
        if self.direction == 'UP':
            new_head['y'] -= BLOCK_SIZE
            if new_head['y'] < 0:
                new_head['y'] = WINDOW_HEIGHT - BLOCK_SIZE
        elif self.direction == 'DOWN':
            new_head['y'] += BLOCK_SIZE
            if new_head['y'] >= WINDOW_HEIGHT:
                new_head['y'] = 0
        elif self.direction == 'LEFT':
            new_head['x'] -= BLOCK_SIZE
            if new_head['x'] < 0:
                new_head['x'] = WINDOW_WIDTH - BLOCK_SIZE
        elif self.direction == 'RIGHT':
            new_head['x'] += BLOCK_SIZE
            if new_head['x'] >= WINDOW_WIDTH:
                new_head['x'] = 0
        
        # Add new head and remove tail
        self.segments.insert(0, new_head)
        self.segments.pop()

    def grow(self):
        """Add a new segment to the snake's tail."""
        # Duplicate the last segment
        tail = self.segments[-1].copy()
        self.segments.append(tail)

    def check_collision(self, food):
        """Check if snake's head collides with food."""
        head = self.segments[0]
        return (head['x'] == food.x and head['y'] == food.y)

    def check_wall_collision(self, width, height):
        """Wrap snake around when it hits screen boundaries."""
        head = self.segments[0]
        
        # Wrap horizontally
        if head['x'] >= width:
            head['x'] = 0
        elif head['x'] < 0:
            head['x'] = width - BLOCK_SIZE
        
        # Wrap vertically
        if head['y'] >= height:
            head['y'] = 0
        elif head['y'] < 0:
            head['y'] = height - BLOCK_SIZE
        
        # Update the head segment
        self.segments[0] = head
        return False  # Never return True since we're wrapping

    def check_self_collision(self):
        """Check if snake's head collides with any of its body segments."""
        head = self.segments[0]
        return any(
            segment != head and
            segment['x'] == head['x'] and
            segment['y'] == head['y']
            for segment in self.segments[1:]
        )

    def draw(self, screen):
        """Render the snake on the screen."""
        # Draw body segments
        for segment in self.segments[1:]:
            pygame.draw.rect(
                screen,
                SNAKE_COLOR,
                pygame.Rect(
                    segment['x'],
                    segment['y'],
                    BLOCK_SIZE,
                    BLOCK_SIZE
                )
            )
        
        # Draw head (different color)
        head = self.segments[0]
        pygame.draw.rect(
            screen,
            SNAKE_HEAD_COLOR,
            pygame.Rect(
                head['x'],
                head['y'],
                BLOCK_SIZE,
                BLOCK_SIZE
            )
        ) 