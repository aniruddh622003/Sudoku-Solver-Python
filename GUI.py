from lib import *

# Visualiser Function. Responsible got GUI handling
def guisolver(puzzle, title):
    while True:

        clear(win)
        # Splash screen cleared after mouse click
        shouldReset = False

        # Draw the retrieved puzzle on the screen
        DrawPuzzle(puzzle, color_rgb(173, 173, 173))
        header = Text(Point(win.getWidth() / 2, 25), title)
        header.setSize(24)
        header.draw(win)

        # Drawing the buttons at the bottom of the screen
        buttonWidth = 100
        buttonHeight = 40

        # Quick Solve button
        solveButton = Rectangle(
            Point((win.getWidth() / 6) - (buttonWidth / 2), win.getHeight() - 65 - buttonHeight / 2),
            Point(win.getWidth() / 6 + buttonWidth / 2 + 40, win.getHeight() - 65 + buttonHeight / 2))
        solveText = Text(Point((win.getWidth() / 6) + 20, win.getHeight() - 65), "Quick Solve")
        solveButton.draw(win)
        solveText.draw(win)

        # Solve with Steps button
        steps = Rectangle(Point((win.getWidth()) - 180, win.getHeight() - 65 - buttonHeight / 2),
                          Point(win.getWidth() - 40, win.getHeight() - 65 + buttonHeight / 2))
        solveText = Text(Point(win.getWidth() - 110, win.getHeight() - 65), "Solve with Steps")
        steps.draw(win)
        solveText.draw(win)

        # Loop until the program should be reset #
        while not shouldReset:
            # Wait for user input
            userInput = win.getMouse()
            # If the user clicks on Quick solve
            if rectangleContains(solveButton, userInput):
                solve(puzzle)  # Solve the puzzle and then draw the puzzle on the screen in darker green
                DrawPuzzle(puzzle, color_rgb(76, 184, 46))
            # If the user clicks on Solve with steps
            elif rectangleContains(steps, userInput):
                solveWithGraphics(puzzle)  # Solve but showing steps
                if solve(puzzle):  # If the puzzle is solvable then print it again showing that the algorithm is done
                    DrawPuzzle(puzzle, color_rgb(79, 94, 255))
                # If the algorithm is not able to find a solution then draw it in red
                else:
                    DrawPuzzle(puzzle, color_rgb(247, 169, 151))
            else:
                buttonPressed = False

