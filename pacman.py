"""Pac-Man: Classic arcade game implemented in Python.

This script runs a simple Pac-Man game using the `turtle` module.
The player controls Pac-Man to collect dots while avoiding ghosts.

Features:
- Customizable board layout.
- Configurable number of ghosts.
- Adjustable Pac-Man speed.
- Basic AI for ghost movement.
"""
from random import choice
from turtle import (
    bgcolor, clear, done, goto, hideturtle, listen, onkey,
    ontimer, setup, tracer, update, up, dot, Turtle
)
from freegames import floor, vector

# Game state variables
state = {'score': 0}
path_drawer = Turtle(visible=False)  # Turtle to draw the board
score_writer = Turtle(visible=False)  # Turtle to display the score
pacman_direction = vector(30, 0)  # Pac-Man's movement direction (30 pixels per move)
pacman_position = vector(-90, -150)  # Initial position of Pac-Man

# List of ghosts with their positions and movement directions
ghosts = [
    [vector(-270, 240), vector(30, 0)],
    [vector(-270, -240), vector(0, 30)],
    [vector(150, 240), vector(0, -30)],
    [vector(150, -240), vector(-30, 0)],
]

# Game board representation (1 = path with dots, 0 = wall)
# fmt: off
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
]
# fmt: on


def draw_square(x, y):
    """Draw a square at the given (x, y) position."""
    path_drawer.up()
    path_drawer.goto(x, y)
    path_drawer.down()
    path_drawer.begin_fill()

    for _ in range(4):
        path_drawer.forward(30)  # Increase cell size to 30
        path_drawer.left(90)

    path_drawer.end_fill()


def get_tile_index(point):
    """Return the index of the tile corresponding to a given point."""
    x = (floor(point.x, 30) + 300) / 30  # Adjusted for 30-pixel cells
    y = (270 - floor(point.y, 30)) / 30   # Adjusted for 30-pixel cells
    return int(x + y * 20)


def is_valid_move(point):
    """Check if the movement is valid (not hitting a wall)."""
    index = get_tile_index(point)
    if tiles[index] == 0:
        return False

    index = get_tile_index(point + 29)  # Check end of the 30-pixel tile
    if tiles[index] == 0:
        return False

    return point.x % 30 == 0 or point.y % 30 == 0


def draw_board():
    """Render the game board."""
    bgcolor('fuchsia')  # Set the background color to fuchsia
    path_drawer.color('blue')

    for index, tile in enumerate(tiles):
        if tile > 0:
            x = (index % 20) * 30 - 300  # Adjusted for 30-pixel tiles
            y = 270 - (index // 20) * 30  # Adjusted for 30-pixel tiles
            draw_square(x, y)

            if tile == 1:
                path_drawer.up()
                path_drawer.goto(x + 15, y + 15)  # Adjust for 30-pixel tile
                path_drawer.dot(5, 'orange')  # Draw dots as orange


def move_characters():
    """Move Pac-Man and ghosts."""
    score_writer.undo()
    score_writer.write(state['score'])

    clear()

    if is_valid_move(pacman_position + pacman_direction):
        pacman_position.move(pacman_direction)

    index = get_tile_index(pacman_position)

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 30 - 300  # Adjusted for 30-pixel tiles
        y = 270 - (index // 20) * 30  # Adjusted for 30-pixel tiles
        draw_square(x, y)

    up()
    goto(pacman_position.x + 15, pacman_position.y + 15)  # Adjust for 30-pixel tile
    dot(30, 'hotpink')  # Pac-Man is pink neon

    # Color the ghosts in electric blue
    ghost_colors = 'deepskyblue'
    for ghost_position, ghost_direction in ghosts:
        if is_valid_move(ghost_position + ghost_direction):
            ghost_position.move(ghost_direction)
        else:
            ghost_direction.x, ghost_direction.y = choice([
                (30, 0), (-30, 0), (0, 30), (0, -30)
            ])

        up()
        goto(ghost_position.x + 15, ghost_position.y + 15)  # Adjust for 30-pixel tile
        dot(30, ghost_colors)  # Ghosts are electric blue

    update()

    for ghost_position, _ in ghosts:
        if abs(pacman_position - ghost_position) < 30:  # Adjust collision size
            return  # Game over if a ghost catches Pac-Man

    ontimer(move_characters, 100)  # Adjust the speed if needed


def change_direction(x, y):
    """Change Pac-Man's direction if the move is valid."""
    if is_valid_move(pacman_position + vector(x, y)):
        pacman_direction.x = x
        pacman_direction.y = y


# Game setup
setup(600, 600, 370, 0)  # Increased screen size to accommodate larger cells
hideturtle()
tracer(False)

# Initialize score display
score_writer.goto(240, 240)
score_writer.color('white')
score_writer.write(state['score'])

# Listen for player input
listen()
onkey(lambda: change_direction(30, 0), 'Right')
onkey(lambda: change_direction(-30, 0), 'Left')
onkey(lambda: change_direction(0, 30), 'Up')
onkey(lambda: change_direction(0, -30), 'Down')

# Start the game
draw_board()
move_characters()
done()
