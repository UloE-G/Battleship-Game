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

    return valid

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

    # Print Letters
    for row in range(len(grid)):
        print(letters(row), end = ")")
        for col in range(len(grid[row])):
            # Print out ship in debug mode
            if debug_mode:
                print("O", end = " ")
            else:
                print(grid[row][col], end = " ")
        print("")
    
    # Print Numbers
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

    is_valid = False
    row = -1
    col = -1
    while is_valid  is False:
        placement = input("Enter row (A-J) and column (0-9) eg. A3: ")
        placement = placement.upper()
        # If user enters to many numbers or letters print error
        if len(placement) <= 0 or len(placement) > 2:
            print("Error: Please enter only one row and column eg. A3")
            continue
        row = placement[0]
        col = placement[1]
        # If row is not a letter or column is not a number print error
        if not row.isalpha() or not col.isnumeric():
            print("Error: Please enter letter (A-J) for row and numebers (0-9) column")
            continue
        # Checks if row is in the grid, if not print error
        row = letters.find(row)
        if not (-1 < row < grid_size):
            print("Error: Please enter letter (A-J) for row and numebers (0-9) column")
            continue
        # Checks if column is in the grid, if not print error
        col =  int(col)
        if not (-1 < col < grid_size):
            print("Error: Please enter letter (A-J) for row and numebers (0-9) column")
            continue
        # If user trys to place a bullet in the exact same location as previous one, print error
        if grid[row][col] == "#" or grid[row][col] == "X":
            print("?... You Have already shot a bullet here, pick somewhere else")
            continue
        # Valid 
        if grid[row][col] == "." or gird[row][col] == "0":
            is_valid = True

    return row, col

def ships_sunk(row, col):
    """
    When all parts of the ship have been hit,
    the ship has sunk.
    """
    global ship_positions
    global grid

    for position in ship_positions:
        start_row = position[0]
        end_row_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row <end_row and start_col <= col <= end_col:
            # Check if all the ship has sunk
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if grid[r][c] != "X":
                        return False
    return True
    
def shot():
    """
    Updates grid and ship based on where the
    bullet was shot.
    """
    global grid
    global sunk
    global bullets

    row, col = bullet_placement()

    print("")
    print("_____________________")

    # Create dialouge to indicate whether user hit, missed, or destroyed a ship
    if grid[row][col] == ".":
        print(":( , You missed, no ship was hit")
    elif grid[row][col] == "O":
        print(":) , you hit!", end=" ")
        grid[row][col] == "X"
        if ships_sunk(row, col):
            print("NICE!!!, A ship has completley sunk")
            sunk += 1
        else:
            print("Good, A ship was shot")
    bullets -= 1

def game_done():
    """
    If all ships have sunk or no more bullets,
    the game ends
    """ 
    global sunk
    global ships
    global bullets
    global game_over

    if ships == ships_sunk:
        print("YOU WON!!!, all ships destroyed")
        game_over = True
    elif bullets <= 0:
        print("YOU FAILED, You didn't destroy all ships and ran out of bullets")
        game_over = True

def main():
    """
    Runs game loop
    """ 
    global  game_over

    create_grid()

    while game_over is False:
        print_grid()
        print("Number of ships remaining: " + str(ships - ships_sunk))
        print("Number of bullets left: " + str(bullets))
        shot()
        print("-----------------------")
        print("")
        game_done()