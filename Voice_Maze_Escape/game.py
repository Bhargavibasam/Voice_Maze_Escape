import pygame
import pyttsx3
import random

# Initialize
pygame.init()
engine = pyttsx3.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Maze Escape Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (70, 130, 180)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)

# Grid settings
TILE_SIZE = 60
ROWS = 7
COLS = 9

# Maze layout
maze = [
    "#########",
    "#     #E#",
    "# ### # #",
    "# #   # #",
    "# ##### #",
    "#       #",
    "#########"
]
maze_grid = [list(row) for row in maze]
player_start = [5, 1]
player_pos = player_start.copy()

# Directions
directions = {
    "UP": (-1, 0, "Moving up"),
    "DOWN": (1, 0, "Moving down"),
    "LEFT": (0, -1, "Moving left"),
    "RIGHT": (0, 1, "Moving right")
}

# Maze tips
maze_tips = [
    "Tip: Try hugging the left wall.",
    "Tip: Look ahead before you move.",
    "Tip: Avoid dead ends by planning your route.",
    "Tip: Sometimes going backward helps go forward.",
    "Tip: Stay calm. Every maze has a way out."
]

def speak(text):
    print("🗣️", text)
    engine.say(text)
    engine.runAndWait()

def draw_maze():
    for row in range(ROWS):
        for col in range(COLS):
            tile = maze_grid[row][col]
            rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if tile == "#":
                pygame.draw.rect(screen, BLACK, rect)
            elif tile == "E":
                pygame.draw.rect(screen, GREEN, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)

def draw_player():
    row, col = player_pos
    rect = pygame.Rect(col * TILE_SIZE + 10, row * TILE_SIZE + 10, TILE_SIZE - 20, TILE_SIZE - 20)
    pygame.draw.rect(screen, BLUE, rect)

# Font and draw button
font = pygame.font.SysFont(None, 28)
def draw_button(label, rect):
    pygame.draw.rect(screen, RED, rect)
    text = font.render(label, True, WHITE)
    text_rect = text.get_rect(center=rect.center)
    screen.blit(text, text_rect)

def move_player(direction_key):
    global player_pos, game_won
    if direction_key not in directions:
        return
    dr, dc, message = directions[direction_key]
    new_r = player_pos[0] + dr
    new_c = player_pos[1] + dc
    if maze_grid[new_r][new_c] == "#":
        speak("Wall ahead. Can't move!")
    else:
        player_pos = [new_r, new_c]
        speak(message)

    if maze_grid[player_pos[0]][player_pos[1]] == "E":
        speak("🎉 You escaped the maze!")
        game_won = True

def reset_game():
    global player_pos, game_won
    player_pos = player_start.copy()
    game_won = False
    speak("Maze reset. Try again!")

# Welcome voice at start
speak("Welcome to the Maze Escape Game! Use the buttons to move and reach the exit.")

# Button positions
button_up = pygame.Rect(270, 460, 80, 40)
button_down = pygame.Rect(270, 510, 80, 40)
button_left = pygame.Rect(180, 510, 80, 40)
button_right = pygame.Rect(360, 510, 80, 40)

yes_button = pygame.Rect(200, 300, 80, 40)
no_button = pygame.Rect(320, 300, 80, 40)

# Game loop
game_running = True
game_won = False

while game_running:
    screen.fill(WHITE)
    draw_maze()
    draw_player()

    if game_won:
        # Draw Yes/No prompt
        msg = font.render("Play Again?", True, BLACK)
        screen.blit(msg, (230, 250))
        draw_button("Yes", yes_button)
        draw_button("No", no_button)
        pygame.display.flip()

        speak("Do you want to play again? Say Yes or No.")

        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    speak("Goodbye!")
                    game_running = False
                    waiting_for_input = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if yes_button.collidepoint(event.pos):
                        reset_game()
                        waiting_for_input = False
                    elif no_button.collidepoint(event.pos):
                        speak("Thanks for playing. Goodbye!")
                        game_running = False
                        waiting_for_input = False
        continue

    # Draw control buttons
    draw_button("Up", button_up)
    draw_button("Down", button_down)
    draw_button("Left", button_left)
    draw_button("Right", button_right)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if not game_won:
                speak("You quit before escaping. Try again next time!")
                speak(random.choice(maze_tips))
            else:
                speak("Goodbye!")
            game_running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_up.collidepoint(event.pos):
                move_player("UP")
            elif button_down.collidepoint(event.pos):
                move_player("DOWN")
            elif button_left.collidepoint(event.pos):
                move_player("LEFT")
            elif button_right.collidepoint(event.pos):
                move_player("RIGHT")

pygame.quit()

