
# For console printing
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - - - -")

        for j in range(len(bo[0])):
            curr = bo[i][j] if bo[i][j] != 0 else " "

            if j == 8:
                print(str(curr) + " | ")
            elif j % 3 == 2 and j != 0:
                print(str(curr) + " || ", end="")

            else:
                print(str(curr) + " | ", end="")


# Finds all empty boxes in the board
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row,column

    return None


# Checks if the number entry in a certain position is valid or not
def valid(bo, num, pos):  # pos = (row,column)
    # check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check square
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


# Actual solving algorithm, used when the solve button is pressed
def solve(bo):
    # Find all empty squares
    find = find_empty(bo)
    # If all boxes are filled, the puzzle is solved
    if not find:
        return True
    # Break variable find into rows and column variable
    else:
        row, column = find

    # Puts 1-9 in each square and check if it is valid
    for i in range(1, 10):
        # If valid, move to the next square
        if valid(bo, i, (row, column)):
            bo[row][column] = i
            # Recursive call, return true from all calls after board is solved
            if solve(bo):
                return True
            # If computer gets stuck, this is the backtracking call, clearing values in the respective square
            bo[row][column] = 0
