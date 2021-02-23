from lib import *
from userin import *
from GUI import guisolver
from puzzles import *
import random

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
#
# Welcome to the Sudoku solver Visualiser. Feel free to take notes as the code is well documented.
# Developed by Aniruddh Dev Upadhyay. :)
# Main motive was to create something that I could watch and kill my time XD
# User input is taken by text file because on the libraries un-ability to style input.
# This is a fairly slow algorithm similar to hit and trial. The complexity is exponential.
# The algorithm can be rectified and refined but I was running out of time and has to do college studies.
# Hope you enjoy the project.
#
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------


def main():
    while True:
        clear(win)
        # Splash Screen
        name = Text(Point(win.getWidth() / 2, 50), "WELCOME TO SUDOKU SOLVER \n By Aniruddh Dev Upadhyay")
        name.setSize(17)
        name.setStyle("bold")
        instructions = Text(Point(win.getWidth() / 2, win.getHeight() / 2 - 50), "This solver uses the backtracking algorithm\n"
                                                                                 "to solve a soduku. It is a pretty simple method\n"
                                                                                 "of traversing the possibility tree and finding\n"
                                                                                 "the solution. If we get stuck on any branch\n"
                                                                                 "because further entries are illegal, then we\n"
                                                                                 "come up a branch and go down a different branch\n"
                                                                                 "in hope to get the valid solution")
        instructions.setFace('courier')
        anyButton = Rectangle(
            Point((win.getWidth())/2-100, win.getHeight()-125),
            Point((win.getWidth()/2)+100, win.getHeight()-75)
        )
        any = Text(Point(win.getWidth() / 2, win.getHeight() - 100), "Click here to get a test")
        any.setFace('arial')
        customButton = Rectangle(
            Point((win.getWidth() / 2) - 100, win.getHeight() / 2 - 25 + 100),
            Point((win.getWidth() / 2) + 100, win.getHeight() / 2 + 25 + 100))
        customText = Text(Point((win.getWidth() / 2), win.getHeight() / 2 + 100), "Custom")
        beginning = [name, instructions, any, anyButton, customButton, customText]
        for item in beginning:
            item.draw(win)
        ui = win.getMouse()
        # If user wants to enter a custom input
        if rectangleContains(customButton, ui):
            userI()

        # If user wants to test
        elif rectangleContains(anyButton, ui):
            clear(win)
            # Imports a random puzzle from puzzles.py file
            i = random.randint(0, 2)
            guisolver(puz_list[i], "Random")


if __name__ == '__main__':
    main()
