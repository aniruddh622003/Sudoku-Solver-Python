from GUI import *
from lib import *


# Creates a screen prompting the user to edit the user.txt file to input sudoku
def userI():
    while True:
        clear(win)
        t = Text(Point((win.getWidth() / 2), win.getHeight()/2-100), "Enter Sudoku in the user.txt\n"
                                                                 "Then click anywhere to continue")
        t.setSize(20)
        t.draw(win)
        a = Text(Point(win.getWidth()/2, win.getHeight()/2+100), "Note: 0 represents an empty cell")
        a.draw(win)
        win.getMouse()

        # Get puzzle from user.txt
        puzzle = getPuzzleFromFile("user.txt")
        # Solve the retrieved puzzle
        guisolver(puzzle, "User - Defined")


if __name__ == '__main__':
    userI()
