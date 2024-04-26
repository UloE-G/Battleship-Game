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

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1

    elif direction == "right":
        if col + length >= grid_size:
            return False
        end_col = col + length

    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1

    elif direction == "down":
        if row + length >= grid_size:
            return False
        end_row = row + length

    return validate_grid_and_place_ship(start_row, end_row, start_col, end_col)

def create_grid():
    """
    Will create a grid and randomly place down ships of 
    different sizes in deiffernet directions.
    """
    global grid
    global grid_size
    global ships
    global ship_positions

    pass

    help_place_ship(0, 0, 0, 0)

def print_grid():
    """
    Prints out the grid
    """

    global grid
    global letters

    pass

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