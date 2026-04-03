from collections import defaultdict

def isValidSudoku(board):
    rowSeen = defaultdict(set)
    colSeen = defaultdict(set)
    squareSeen = defaultdict(set)
    squareRow = 0
    squareCol = 1


    for rowNum in range(0,9):
        if rowNum > 2:
            squareRow = 3
        if rowNum > 5:
            squareRow = 6

        row = board[rowNum]
        for colNum in range(0, 9):
            if colNum <= 8:
                squareCol = 3
            if colNum <= 5:
                squareCol = 2
            if colNum <=2:
                squareCol = 1
            squareNum = squareRow + squareCol

            numSeen = row[colNum]
            if numSeen == ".":
                continue
            if numSeen in rowSeen[rowNum]:
                return False
            rowSeen[rowNum].add(numSeen)

            if numSeen in colSeen[colNum]:
                return False
            colSeen[colNum].add(numSeen)

            if numSeen in squareSeen[squareNum]:
                return False
            squareSeen[squareNum].add(numSeen)
        
    return True


def isValidSudokuAns(board):
    rowSeen = defaultdict(set)
    colSeen = defaultdict(set)
    squareSeen = defaultdict(set)

    for rowNum in range(9):
        for colNum in range(9):
            squareNum = (rowNum // 3) * 3 + (colNum // 3)
            numSeen = board[rowNum][colNum]

            if numSeen == ".":
                continue

            if numSeen in rowSeen[rowNum]:
                return False
            rowSeen[rowNum].add(numSeen)

            if numSeen in colSeen[colNum]:
                return False
            colSeen[colNum].add(numSeen)

            if numSeen in squareSeen[squareNum]:
                return False
            squareSeen[squareNum].add(numSeen)
        
    return True

def isValidSudokuRe(board):
    rowSeen = defaultdict(set)
    colSeen = defaultdict(set)
    boxSeen = defaultdict(set)


    for r in range(len(board)):
        for c in range(len(board[0])):
            boxNum = (r // 3) * 3 + c // 3
            num = board[r][c]
            if num == '.':
                continue

            if num in rowSeen[r]:
                return False
            rowSeen[r].add(num)

            if num in colSeen[c]:
                return False
            colSeen[c].add(num)

            if num in boxSeen[boxNum]:
                return False
            boxSeen[boxNum].add(num)
    
    return True
    
    print(rowSeen)


            


board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudokuRe(board))