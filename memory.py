"""Memory, puzzle game of number pairs.
Exercises:
1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""
from random import *    # Imports all functions from the random module
from turtle import *    # Imports all functions from the turtle graphics module
from freegames import path    # Imports the path function from freegames package

car = path('car.gif')    # Loads the car image to be used as background
tiles = list(range(32)) * 2    # Creates a list of numbers 0-31, each appearing twice (64 total)
state = {'mark': None}    # Dictionary to keep track of the currently selected tile
hide = [True] * 64    # List tracking which tiles are hidden (all start as hidden)

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()    # Lifts the pen to move without drawing
    goto(x, y)    # Moves turtle to the specified coordinates
    down()    # Puts the pen down to start drawing
    color('black', 'white')    # Sets outline color to black, fill color to white
    begin_fill()    # Begins the fill operation
    for count in range(4):    # Draws a square by moving forward and turning left 4 times
        forward(50)    # Each side is 50 pixels
        left(90)    # Turns 90 degrees left
    end_fill()    # Completes the fill operation

def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    # Calculates the tile index from screen coordinates
    # +200 adjusts for the coordinate system offset
    # //50 converts pixels to tile units (each tile is 50x50)
    # *8 for the row calculation accounts for 8 tiles per row
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    # Converts a tile index back to screen coordinates
    # count % 8 gives the column position (0-7)
    # count // 8 gives the row position (0-7)
    # *50 converts tile units to pixels
    # -200 adjusts for the coordinate system offset
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)    # Converts tap coordinates to a tile index
    mark = state['mark']    # Gets the currently marked tile (if any)
    
    # Logic for handling tile selection:
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        # If no tile is currently selected, or
        # If the same tile is clicked again, or
        # If the selected tiles don't match
        state['mark'] = spot    # Mark the clicked tile
    else:
        # If the tiles match
        hide[spot] = False    # Reveal the current tile
        hide[mark] = False    # Reveal the previously marked tile
        state['mark'] = None    # Clear the mark

def draw():
    """Draw image and tiles."""
    clear()    # Clears the screen for redrawing
    goto(0, 0)    # Moves to the center of the screen
    shape(car)    # Sets the turtle shape to the car image
    stamp()    # Stamps the car image onto the background
    
    # Draw all hidden tiles
    for count in range(64):    # Loops through all 64 tile positions
        if hide[count]:    # Only draws tiles that are still hidden
            x, y = xy(count)    # Gets the screen coordinates for this tile
            square(x, y)    # Draws a square at those coordinates
    
    # Handle the currently marked tile
    mark = state['mark']    # Gets the currently marked tile (if any)
    if mark is not None and hide[mark]:    # If a tile is marked and it's hidden
        x, y = xy(mark)    # Gets the screen coordinates for the marked tile
        up()    # Lifts the pen
        goto(x + 2, y)    # Moves to a position slightly offset from the tile's corner
        color('black')    # Sets text color to black
        write(tiles[mark], font=('Arial', 30, 'normal'))    # Writes the tile's value
    
    update()    # Updates the screen with all the changes
    ontimer(draw, 100)    # Schedules the draw function to run again in 100ms

shuffle(tiles)    # Randomly shuffles the tile values before starting the game
setup(420, 420, 370, 0)    # Sets up the screen dimensions and position
addshape(car)    # Registers the car image as a valid turtle shape
hideturtle()    # Hides the turtle cursor
tracer(False)    # Turns off animation updates for smoother drawing
onscreenclick(tap)    # Registers the tap function to handle mouse clicks
draw()    # Starts the drawing loop
done()    # Enters the main event loop
