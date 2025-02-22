"""
Configuration Constants
Contains all game settings and configuration values.
"""

# Window Settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Snake Game"
FPS = 60

# Game Colors (R, G, B)
BACKGROUND_COLOR = (0, 0, 0)       # Black
SCORE_COLOR = (255, 255, 255)      # White
GAME_OVER_COLOR = (255, 0, 0)      # Red
SNAKE_COLOR = (0, 255, 0)          # Green
SNAKE_HEAD_COLOR = (0, 200, 0)     # Darker Green
FOOD_COLOR = (255, 0, 0)           # Red

# Font Settings
SCORE_FONT_SIZE = 32
GAME_OVER_FONT_SIZE = 64

# Game Grid Settings
BLOCK_SIZE = 20  # Size of each grid cell in pixels

# Snake Settings
INITIAL_SNAKE_LENGTH = 3
MOVEMENT_SPEED = BLOCK_SIZE  # Pixels per movement

# Calculate initial snake position (center of screen)
INITIAL_POSITION_X = (WINDOW_WIDTH // BLOCK_SIZE // 2) * BLOCK_SIZE
INITIAL_POSITION_Y = (WINDOW_HEIGHT // BLOCK_SIZE // 2) * BLOCK_SIZE

# Ensure initial position aligns with grid
assert INITIAL_POSITION_X % BLOCK_SIZE == 0, "Initial X position must align with grid"
assert INITIAL_POSITION_Y % BLOCK_SIZE == 0, "Initial Y position must align with grid"

# Ensure window dimensions are multiples of block size
assert WINDOW_WIDTH % BLOCK_SIZE == 0, "Window width must be a multiple of block size"
assert WINDOW_HEIGHT % BLOCK_SIZE == 0, "Window height must be a multiple of block size"

# Game Speed Settings
BASE_FPS = 8  # Starting speed (lower means slower)
SPEED_INCREMENT = 1  # How much to increase speed per score point
MAX_FPS = 30  # Maximum speed cap 