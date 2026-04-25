def searchMatrix(matrix, target):
    rowL = 0
    rowR = len(matrix) -1
    

    while rowL <= rowR:
        rowM = rowL + (rowR - rowL) // 2
        currRow = matrix[rowM]
        if currRow[0] > target:
            rowR = rowM - 1
        elif currRow[-1] < target:
            rowL = rowM + 1
        else:
            i = 0
            j = len(currRow) -1
            while i <= j:
                m = i + (j-i) // 2
                if currRow[m] == target:
                    return True
                elif currRow[m] > target:
                    j = m - 1
                elif currRow[m] < target:
                    i = m + 1
            
            return False
    return False
