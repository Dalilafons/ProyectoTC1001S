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
pacman_direction = vector(5, 0)  # Pac-Man's movement direction
pacman_position = vector(-40, -80)  # Initial position of Pac-Man

# List of ghosts with their positions and movement directions
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
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
        path_drawer.forward(20)
        path_drawer.left(90)

    path_drawer.end_fill()


def get_tile_index(point):
    """Return the index of the tile corresponding to a given point."""
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    return int(x + y * 20)


def is_valid_move(point):
    """Check if the movement is valid (not hitting a wall)."""
    index = get_tile_index(point)
    if tiles[index] == 0:
        return False

    index = get_tile_index(point + 19)
    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0


def draw_board():
    """Render the game board."""
    bgcolor('black')
    path_drawer.color('blue')

    for index, tile in enumerate(tiles):
        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            draw_square(x, y)

            if tile == 1:
                path_drawer.up()
                path_drawer.goto(x + 10, y + 10)
                path_drawer.dot(2, 'white')  # Draw dots for Pac-Man to collect


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
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        draw_square(x, y)

    up()
    goto(pacman_position.x + 10, pacman_position.y + 10)
    dot(20, 'yellow')  # Draw Pac-Man

    for ghost_position, ghost_direction in ghosts:
        if is_valid_move(ghost_position + ghost_direction):
            ghost_position.move(ghost_direction)
        else:
            ghost_direction.x, ghost_direction.y = choice([
                (5, 0), (-5, 0), (0, 5), (0, -5)
            ])

        up()
        goto(ghost_position.x + 10, ghost_position.y + 10)
        dot(20, 'red')  # Draw ghosts

    update()

    for ghost_position, _ in ghosts:
        if abs(pacman_position - ghost_position) < 20:
            return  # Game over if a ghost catches Pac-Man

    ontimer(move_characters, 100)  # Adjust the speed if needed


def change_direction(x, y):
    """Change Pac-Man's direction if the move is valid."""
    if is_valid_move(pacman_position + vector(x, y)):
        pacman_direction.x = x
        pacman_direction.y = y


# Game setup
setup(420, 420, 370, 0)
hideturtle()
tracer(False)

# Initialize score display
score_writer.goto(160, 160)
score_writer.color('white')
score_writer.write(state['score'])

# Listen for player input
listen()
onkey(lambda: change_direction(5, 0), 'Right')
onkey(lambda: change_direction(-5, 0), 'Left')
onkey(lambda: change_direction(0, 5), 'Up')
onkey(lambda: change_direction(0, -5), 'Down')

# Start the game
draw_board()
move_characters()
done()
