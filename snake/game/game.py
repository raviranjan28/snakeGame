"""
Game Class Module
Handles the main game loop, collision detection, and game state management.
"""

import pygame
from .snake import Snake
from .food import Food
from .config import (
    FPS,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    BACKGROUND_COLOR,
    SCORE_FONT_SIZE,
    SCORE_COLOR,
    GAME_OVER_FONT_SIZE,
    GAME_OVER_COLOR,
    BASE_FPS,
    SPEED_INCREMENT,
    MAX_FPS
)

class Game:
    def __init__(self, screen):
        """Initialize the game state and objects."""
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False
        self.score = 0

        # Initialize game objects
        self.snake = Snake()
        self.food = Food()

        # Initialize sounds with error handling
        pygame.mixer.init()
        try:
            self.eat_sound = pygame.mixer.Sound("assets/sounds/eat.wav")
            self.game_over_sound = pygame.mixer.Sound("assets/sounds/game_over.wav")
            self.use_sounds = True
        except (pygame.error, FileNotFoundError):
            print("Sound files not found. Running without sound.")
            self.use_sounds = False

        # Initialize fonts
        pygame.font.init()
        self.score_font = pygame.font.Font(None, SCORE_FONT_SIZE)
        self.game_over_font = pygame.font.Font(None, GAME_OVER_FONT_SIZE)

        # Add current game speed tracking
        self.current_fps = BASE_FPS

        # Add pause state
        self.paused = False

    def handle_events(self):
        """Process pygame events (keyboard, quit, etc.)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.game_over:
                        self.reset_game()
                    else:
                        # Toggle pause state
                        self.paused = not self.paused
                elif not self.game_over and not self.paused:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction('UP')
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction('DOWN')
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction('LEFT')
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction('RIGHT')

    def update(self):
        """Update game objects and check for collisions."""
        if self.game_over or self.paused:  # Don't update if paused
            return

        # Move snake
        self.snake.move()

        # Check for collision with food
        if self.snake.check_collision(self.food):
            self.score += 1
            if self.use_sounds:
                self.eat_sound.play()
            self.snake.grow()
            self.food.respawn()
            
            # Update game speed based on score
            self.current_fps = min(BASE_FPS + (self.score * SPEED_INCREMENT), MAX_FPS)

        # Check for self collision only (removed wall collision)
        if self.snake.check_self_collision():
            self.game_over = True
            if self.use_sounds:
                self.game_over_sound.play()

    def draw(self):
        """Draw all game objects and UI elements."""
        # Clear screen
        self.screen.fill(BACKGROUND_COLOR)

        # Draw game objects
        self.food.draw(self.screen)
        self.snake.draw(self.screen)

        # Draw score
        score_text = self.score_font.render(f"Score: {self.score}", True, SCORE_COLOR)
        self.screen.blit(score_text, (10, 10))

        # Draw game over message if applicable
        if self.game_over:
            game_over_text = self.game_over_font.render(
                "Game Over! Press SPACE to restart", True, GAME_OVER_COLOR
            )
            text_rect = game_over_text.get_rect(
                center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            )
            self.screen.blit(game_over_text, text_rect)
        # Draw pause message if game is paused
        elif self.paused:
            pause_text = self.game_over_font.render(
                "PAUSED", True, SCORE_COLOR
            )
            text_rect = pause_text.get_rect(
                center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            )
            self.screen.blit(pause_text, text_rect)

        # Update display
        pygame.display.flip()

    def reset_game(self):
        """Reset the game state for a new game."""
        self.game_over = False
        self.score = 0
        self.current_fps = BASE_FPS  # Reset speed to initial value
        self.snake = Snake()
        self.food.respawn()

    def run(self):
        """Main game loop."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.current_fps)  # Use current_fps instead of FPS 