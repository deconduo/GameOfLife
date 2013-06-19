# Game Of Life

'''Imports'''

# For random distribution of cells
from random import choice

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
        print i
        if self.isAliveBool == True:
            if (i < 2) or (i > 3):
                self.willLiveBool = False
                print "Cell Dying"
        if self.isAliveBool == False:
            if i == 3:
                self.willLiveBool = True
                print "Cell Living"

    # Changes the cell state
    def doNextStep(self):
        self.isAliveBool = self.willLiveBool
        self.willLiveBool = False


'''Functions'''

# Sets up a blank grid
def setUpGrid(n, m, grid):
    i = 0
    j = 0
    while j < m :
        while i < n:
            grid.append(cell(i, j, False))
            i += 1
        i = 0
        j += 1    

# Places the given number of cells randomly on the board
def randomlyPlaceLivingCells(n, grid):
    i = 0
    while i < n:
        x = choice(grid)
        if x.isAliveBool == False:
            x.isAliveBool = True
            i += 1

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
        if ((otherCells.xPosInt == cell.xPosInt) or (otherCells.xPosInt == cell.xPosInt + 1) or (otherCells.xPosInt == cell.xPosInt -1)) and ((otherCells.yPosInt == cell.yPosInt) or (otherCells.yPosInt == cell.yPosInt + 1) or (otherCells.yPosInt == cell.yPosInt -1)) and (otherCells.isAliveBool == True):
            i += 1
    if cell.isAliveBool == True:
        return (i-1)
    else:
        return i
        
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

myGrid = []
setUpGrid(10, 10, myGrid)
randomlyPlaceLivingCells(50, myGrid)
printTheGrid(myGrid)
print "\n"
nextStep(myGrid)
print "\n"
nextStep(myGrid)
print "\n"
nextStep(myGrid)

