"""Memory, puzzle game of number pairs.
Exercises:
1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
6. Count and display the number of pairs discovered.
"""
from random import *    # Imports all functions from the random module
from turtle import *    # Imports all functions from the turtle graphics module
from freegames import path    # Imports the path function from freegames package

car = path('car.gif')    # Loads the car image to be used as background
tiles = list(range(8)) * 2    # Creates a list of numbers 0-7, each appearing twice (16 total)
state = {'mark': None}    # Dictionary to keep track of the currently selected tile
hide = [True] * 16    # List tracking which tiles are hidden (all start as hidden)
pairs_found = 0    # Counter for the number of pairs found
game_complete = False    # Flag to track if the game is complete
tap_count = 0    # Counter for the number of taps

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
    # Adjusted for a 4x4 grid (4 columns)
    return int((x + 100) // 50 + ((y + 100) // 50) * 4)

def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    # Adjusted for a 4x4 grid (4 columns)
    return (count % 4) * 50 - 100, (count // 4) * 50 - 100

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global pairs_found, game_complete, tap_count    # Access the global counters
    
    # Don't process taps if game is already complete
    if game_complete:
        return
    
    # Increment tap counter
    tap_count += 1
    print(f"Tap count: {tap_count}")
        
    spot = index(x, y)    # Converts tap coordinates to a tile index
    
    # Check if the tap is within the valid grid area
    if spot < 0 or spot >= 16:
        return
        
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
        pairs_found += 1    # Increment the pairs found counter
        
        # Check if all pairs have been found (8 pairs total)
        if pairs_found == 8:
            game_complete = True
            print("¡Felicidades! Has encontrado todos los pares.")

def draw():
    """Draw image and tiles."""
    clear()    # Clears the screen for redrawing
    goto(0, 0)    # Moves to the center of the screen
    shape(car)    # Sets the turtle shape to the car image
    stamp()    # Stamps the car image onto the background
    
    # Draw all hidden tiles
    for count in range(16):    # Loops through all 16 tile positions
        if hide[count]:    # Only draws tiles that are still hidden
            x, y = xy(count)    # Gets the screen coordinates for this tile
            square(x, y)    # Draws a square at those coordinates
    
    # Handle the currently marked tile
    mark = state['mark']    # Gets the currently marked tile (if any)
    if mark is not None and hide[mark]:    # If a tile is marked and it's hidden
        x, y = xy(mark)    # Gets the screen coordinates for the marked tile
        up()    # Lifts the pen
        # Center single-digit numbers in the tile
        goto(x + 20, y + 5)    # Centers the digit in the tile
        color('black')    # Sets text color to black
        write(tiles[mark], font=('Arial', 30, 'normal'), align='center')    # Writes the tile's value centered
    
    # Display the number of pairs found
    up()    # Lifts the pen
    goto(-95, -95)    # Positions the text at the bottom left
    color('blue')    # Sets text color to blue
    write(f"Pairs found: {pairs_found} / 8", font=('Arial', 12, 'normal'))    # Writes the pairs counter
    
    # Display tap count
    up()
    goto(-95, -120)
    color('purple')
    write(f"Taps: {tap_count}", font=('Arial', 12, 'normal'))
    
    # Display completion message when game is complete
    if game_complete:
        up()
        goto(0, 0)    # Position in the center of screen
        color('green')
        write("¡JUEGO COMPLETADO!", font=('Arial', 18, 'bold'), align='center')
    
    update()    # Updates the screen with all the changes
    ontimer(draw, 100)    # Schedules the draw function to run again in 100ms

shuffle(tiles)    # Randomly shuffles the tile values before starting the game
setup(220, 220, 370, 0)    # Sets up the screen dimensions and position for 4x4 grid
addshape(car)    # Registers the car image as a valid turtle shape
hideturtle()    # Hides the turtle cursor
tracer(False)    # Turns off animation updates for smoother drawing
onscreenclick(tap)    # Registers the tap function to handle mouse clicks
draw()    # Starts the drawing loop
done()    # Enters the main event loop