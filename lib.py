from graphics import *
from solver import *
# With of each square in the sudoku
sq_width = 50

# Margin between left and right and each 3x3 block
margin = 10

# Make a new window
win = GraphWin('Sudoku Solver', margin * 4 + sq_width * 9 + 1, 200 + sq_width * 9 + 1)

def clear(win):
    # Undraws all items on the window
    for item in win.items[:]:
        item.undraw()
    win.update()


# Draw a block and arrange it into the grid. Also write number in it if not empty
def drawBlock(row: int, col: int, val: int, color):
    # Args
    # row (int): row of block to draw
    # col (int): col of block to draw
    # val (int): value to place in the block - 0 if empty
    # color (string): string to represent color for the block
    global win
    # Vertical 3x3 the block belongs to
    verticalblock = row // 3 + 1
    verticalDiff = verticalblock * margin + 50
    # Horizontal 3x3 the block belongs to
    horizontalblock = col // 3 + 1
    horizontalDiff = horizontalblock * margin
    # Creating the block
    upperLeft = Point(col * sq_width, row * sq_width)
    upperLeft.move(horizontalDiff, verticalDiff)
    bottomRight = Point((col + 1) * sq_width, (row + 1) * sq_width)
    bottomRight.move(horizontalDiff, verticalDiff)
    block = Rectangle(upperLeft, bottomRight)
    block.setFill(color)
    block.draw(win)

    if val != 0:
        # Write number if the value is not 0
        textPoint = Point(col * sq_width + sq_width / 2, row * sq_width + sq_width / 2)
        textPoint.move(horizontalDiff, verticalDiff)
        numberImage = Text(textPoint, str(val))
        numberImage.setSize(20)
        numberImage.draw(win)


# Solve with Steps function
def solveWithGraphics(puzzle):
    # Lag the animation intentionally, as it will become very fast, this value can be tweaked to add or reduce latency
    time.sleep(0.05)
    # Find the next empty spot
    firstEmpty = find_empty(puzzle)
    # If there are no empty spots left, means the puzzle is solved
    if not firstEmpty:
        return True
    # If not, return the position of empty block
    row, col = firstEmpty
    # Try values 1-9 in each empty block
    for val in range(1, 10):
        # Check for a valid placement
        if valid(puzzle, val, (row, col)):
            puzzle[row][col] = val
            drawBlock(row, col, val, color_rgb(93, 205, 252))
            # Recursive call, return true if the correct solution is reached
            if solveWithGraphics(puzzle):
                return True
            # If computer gets stuck, back-track!!
            puzzle[row][col] = 0
            drawBlock(row, col, 0, color_rgb(255, 97, 79))
            # Backtracking delay, similar to first sleep function just works on backtrack
            time.sleep(0.000)
    return False


def rectangleContains(rect: Rectangle, p: Point):
    # Checks if user clicked within a button
    x = p.getX()
    y = p.getY()
    return rect.getP1().getX() <= x <= rect.getP2().getX() and rect.getP1().getY() <= y <= rect.getP2().getY()


def DrawPuzzle(puzzle: list, color):
    # Iterating through the 9x9 matrix
    for row in range(9):
        for col in range(9):
            # Draw empty square if value is 0
            if puzzle[row][col] == 0:
                drawBlock(row, col, puzzle[row][col], 'white')
            # Draws block with defined color and value if block holds a value
            else:
                drawBlock(row, col, puzzle[row][col], color)


def getPuzzleFromFile(fileName: str):
    # Open file in read mode
    f = open(fileName, "r")
    # Initial an empty variable
    puzzle = []
    # populate puzzle
    for i in range(9):
        line = f.readline()
        lineArray = [int(c) for c in line if not (c == ' ' or c == '\n')]
        puzzle.append(lineArray)
    return puzzle

