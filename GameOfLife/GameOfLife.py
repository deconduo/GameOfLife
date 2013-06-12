# Game Of Life

'''Imports'''

# For random distribution of cells
import random

'''Classes'''

# Defines the cell class
class cell(object):
    # Initialization function
    def __init__(self, xPos, yPos, isAlive=False, willLive=False):
        self.xPosInt = xPos
        self.yPosInt = yPos
        self.isAliveBool = isAlive
        self.willLiveBool = willLive
    
    # Checks if cell state will change with next step    
    def checkNextStep(self, grid):
        i = getAdjacentCells(self, grid)
        if self.isAliveBool == True:
            if (i < 2) or (i > 3):
                self.willLiveBool = False
        if self.isAliveBool == False:
            if i == 3:
                self.willLiveBool = True

    # Changes the cell state
    def doNextStep(self):
        self.isAliveBool = self.willLiveBool


'''Functions'''

# Prints the grid to the screen
def printTheGrid(grid):
    gridString = ""
    currentRow = 0
    for cell in grid:
        if cell.yPosInt != currentRow:
            gridString += "\n"
            currentRow += 1
        if cell.isAliveBool == True:
            gridString += "*"
        else:
            gridString += "-"
    print gridString

# Calculates the number of adjacent living cells for a given cell
def getAdjacentCells(cell, grid):
    i = 0
    for otherCells in grid:
        if (otherCells.xPosInt == (cell.xPosInt + 1 | cell.xPosInt | cell.xPosInt - 1)) & (otherCells.yPosInt == (cell.yPosInt + 1 | cell.yPosInt | cell.yPosInt - 1)):
            i += 1
    return i
        

# Places the given number of cells randomly on the board
def randomlyPlaceLivingCells():
    pass

# Advances the board by one step
def nextStep(grid):
    for cell in grid:
        cell.checkNextStep(grid)
    for cell in grid:
        cell.doNextStep()
    printTheGrid(grid)

# Checks if the grid is empty
def isEmptyGrid(grid):
    isEmpty = True
    for cell in grid:
        if cell.isAliveBool == True:
            isEmpty = False
    return isEmpty

'''Main Program'''

myGrid = [cell(0, 0, True), cell(1, 0, False), cell(0, 1, False), cell(1, 1, False)]
printTheGrid(myGrid)
nextStep(myGrid)
