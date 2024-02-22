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

        if testCol == currentSolution[row]:
            # Check if any piece is directly above
            # goes to current solution board, index is the row so it checks if the col is the same
            return False
        
        if abs(testRow - row) == abs(testCol - currentSolution[row]):
            # checks any diagonal solutions
            # if the # of rows above the current position is == to the number of columns away from the current position,
            # it is diagonal
            return False
        
        return True
    
    # Loop, "Bad Solution"

    for queen0 in range(numQueens):
        if not isSafe(0, queen0):
            # uses helper method to check current row and column
            # queen0 is the changing column per loop of this
            continue
        else:
            # stores a valid position into the currentSolution list
            currentSolution[0] = queen0

        # THEN loop through next queen position
        
        for queen1 in range(numQueens):
            if not isSafe(1, queen1):
                continue
            else:
                currentSolution[1] = queen1

            for queen2 in range(numQueens):
                if not isSafe(2, queen2):
                    continue
                else:
                    currentSolution[2] = queen2
                
                for queen3 in range(numQueens):
                    if not isSafe(3, queen3):
                        continue
                    else:
                        currentSolution[3] = queen3

                    for queen4 in range(numQueens):
                        if not isSafe(4, queen4):
                            continue
                        else:
                            currentSolution[4] = queen4

                        for queen5 in range(numQueens):
                            if not isSafe(5, queen5):
                                continue
                            else:
                                currentSolution[5] = queen5

                            for queen6 in range(numQueens):
                                if not isSafe(6, queen6):
                                    continue
                                else:
                                    currentSolution[6] = queen6

                                for queen7 in range(numQueens):
                                    if not isSafe(7, queen7):
                                        continue
                                    else:
                                        currentSolution[7] = queen7
                                        solutions.append(currentSolution.copy())

    print(len(solutions)," solutions found.")
    for solution in solutions:
        print(solution)
