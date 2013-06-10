# Game Of Life

'''Classes'''

class cell(object):
    def __init__(self, xPos, yPos, isAlive, willLive=False):
        self.xPosInt = xPos
        self.yPosInt = yPos
        self.isAliveBool = isAlive
        self.willLiveBool = willLive
        
    def checkNextStep(self):
        if self.isAliveBool == True:
            if getAdjacentCells(self) < 2 or getAdjacentCells(self) > 3:
                self.willLiveBool = False
        if self.isAliveBool == False:
            if getAdjacentCells(self) == 3:
                self.willLiveBool = True

    def doNextStep(self):
        self.isAliveBool = self.willLiveBool


'''Functions'''

# Prints the grid to the screen
def printTheGrid(cellList):
    for cell in cellList:
        if cell.isAliveBool == True:
            print "*"
        else:
            print "-"

# Calculates the number of adjacent living cells for a given cell
def getAdjacentCells():
    pass

# Places the given number of cells randomly on the board
def randomlyPlaceLivingCells():
    pass

# Advances the board by one step
def nextStep():
    pass

# Checks if the grid is empty
def isEmptyGrid(cellList):
    n = False
    for cell in cellList:
        if cell.isAliveBool() == True:
            n = True
    return n

'''Main Program'''

grid = [cell(0, 0, True), cell(0, 1, False), cell(1, 0, False), cell(1, 1, False)]
printTheGrid(grid)