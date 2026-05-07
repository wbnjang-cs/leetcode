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

def searchMatrixRe(matrix, target):
    rowL = 0
    rowR = len(matrix) - 1

    while rowL <= rowR:
        rowM = rowL + (rowR - rowL) // 2
        row = matrix[rowM]
        if row[0] <= target and target <= row[-1]:
            l = 0
            r = len(row) - 1

            while l <= r:
                m = l + (r - l) // 2

                if row[m] == target:
                    return True
                elif row[m] < target:
                    l = m + 1
                else:
                    r = m - 1

            return False
        
        elif target < row[0]:
            rowR = rowM - 1
        elif target > row[-1]:
            rowL = rowM + 1
    
    return False