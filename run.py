import random 
import time

# Global Variables
grid = [[]]
grid_size = 10
ships = 4
bullets = 20
game_over = False
sunk = 0
ship_positions = [[]]
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def validate_ship(start_row, end_row, start_col, end_col):
    """
    Will check to see if it is valid to place a ship in a specific row or column 
    """
    global grid
    global ship_positions
    
    # Checks to see if all the spots on the ship water or empty space (".")
    valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            # Breaks out of loop if it runs into something that is not "."
            if grid[r][c] != ".":
                valid = False
                break
    # Creates ships if all positions are "."
    if valid:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid[r][c] = "O"

    return all_valid:

def help_place_ship(row, col, direction, lenght):
    """
    Based on the direction, will help to try and place ship on the grid
    """
    global grid_size

    # Checks each row and column one time
    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1

    # Checks to see if the grid starting position to the left is actually on the grid
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1

    # Checks to see if the grid starting position to the right is actually on the grid
    elif direction == "right":
        if col + length >= grid_size:
            return False
        end_col = col + length

    # Checks to see if the grid starting position up is actually on the grid
    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1

    # Checks to see if the grid starting position down is actually on the grid
    elif direction == "down":
        if row + length >= grid_size:
            return False
        end_row = row + length

    return validate_ship(start_row, end_row, start_col, end_col)

def create_grid():
    """
    Will create a grid and randomly place down ships of 
    different sizes in deiffernet directions.
    """
    global grid
    global grid_size
    global ships
    global ship_positions

    random.seed(time.time())

    rows, cols = (grid_size, grid_size)

    grid = []
    # Creats an empty row
    for r in range(rows):
        row = []
        # Places a "." in each row
        for c in range(cols):
            row.append(".")
        # Places row in gird
        grid.append(row)

    ships_placed = 0

    ship_positions = []

    # Radomize ship placement
    while ships_placed != ships:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)
        if help_place_ship(random_row, random_col, direction, ship_size):
            num_of_ships_placed += 1

def print_grid():
    """
    Prints out the grid
    """
    global grid
    global letters

    # For testing
    debug_mode = True

    # Slicing letters
    letters = letters[0: len(grid) + 1]

    for row in range(len(grid)):
        print(letters(row), end = ")")
        for col in range(len(grid[row])):
            if debug_mode:
                print("O", end = " ")
            else:
                print(grid[row][col], end = " ")
        print("")
    
    print(" ", end = " ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")

def bullet_placement():
    """
    Check if row and column the bullet is going is valid
    """
    global letters
    global grid

    pass

    return 0, 0

def ships_sunk(row, col):
    """
    When all parts of the ship have been hit,
    the ship has sunk.
    """
    global ship_positions
    global grid

    pass

def shot():
    """
    Updates grid and ship based on where the
    bullet was shot.
    """
    global grid
    global ships_sunk
    global bullets

    row, col = bullet_placement()

    pass

def game_done():
    """
    If all ships have sunk or no more bullets,
    the game ends
    """ 
    global ships_sunk
    global ships
    global bullets
    global game_over

    pass

def main():
    """
    Runs game loop
    """ 
    global  game_over

    pass