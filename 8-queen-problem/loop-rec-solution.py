# 8 Queen Problem
# "Dirty" slow way with nested for loops

numQueens = 8

currentSolution = [0 for x in range( numQueens )] # initialize list with 8 0s to represent spaces in the solution
solutions = [] # once currentSolution is filled, append into solutions list

print(currentSolution)

# helper method that figures out if a position is safe on the current row

def isSafe(testRow, testCol):
    if testRow == 0:
        return True

    for row in range(0, testRow):
        # loops through each row

        # Check if any piece is directly above

        if testCol == currentSolution[row]:
            # goes to current solution board, index is the row so it checks if the col is the same
            return False
        
        if abs(testRow - row) == abs(testCol - currentSolution[row]):
            # checks any diagonal solutions
            # if the # of rows above the current position is == to the number of columns away from the current position,
            # it is diagonal
            return False
        
        return True
