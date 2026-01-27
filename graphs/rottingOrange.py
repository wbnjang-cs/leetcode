from collections import deque

def orangesRotting(grid):
    q = deque()
    seen = set()
    min = -1
    hor = len(grid[0])
    ver = len(grid)
    numFresh = 0

    for i in range(ver):
        for j in range(hor):
            if grid[i][j] == 0:
                seen.add((i,j))
            if grid[i][j] == 1:
                numFresh +=1
            if grid[i][j] == 2:
                q.append((i,j))
    

    if numFresh == 0:
        return 0
    
    def spread(r,c):
        if r<0 or c<0 or r >= ver or c>= hor or (r,c) in seen:
            return
        seen.add((r,c))
        q.append((r,c))

    while q:
        print(f"starting at q = {q} and seen = {seen} at minute {min}")
        for orange in range(len(q)):
            r,c = q.popleft()
            seen.add((r,c))
            if grid[r][c] != 0:
                spread(r+1,c)
                spread(r,c+1)
                spread(r,c-1)
                spread(r-1,c)
            

        min +=1
        print(f"ended at q = {q} and seen = {seen} at minute {min}" )






    if hor * ver != len(seen):
        return -1
    return min
            


def orangesRottingAnswer():
    q = deque()
    minutes = 0
    cols = len(grid[0])
    rows = len(grid)
    numFresh = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                numFresh +=1
            if grid[r][c] == 2:
                q.append((r,c))
    
    if numFresh == 0:
        return 0
    
    dirs = [(1,0), (0,1), (-1,0), (0,-1)]

    while q and numFresh > 0:
        for orange in range(len(q)):
            r,c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    numFresh -=1
                    q.append((nr,nc))
        
        minutes +=1
    
    return minutes if numFresh == 0 else -1


def rottingOrangesAnswer(grid):
    q = deque()
    minutes = 0
    seen = set()
    cols = len(grid[0])
    rows = len(grid)
    freshNum = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                freshNum +=1
            elif grid[r][c] == 2:
                q.append((r,c)) 
    
    if freshNum == 0:
        return 0
    
    dr = [(1,0),(0,1),(-1,0),(0,-1)]

    while q and freshNum > 0:
        minutes +=1
        for pair in range(len(q)):
            r, c = q.popleft()
            for dirR, dirC in dr:
                newR, newC = r + dirR, c + dirC
                if 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] == 1:
                    q.append((newR, newC))
                    freshNum -=1
                    grid[newR][newC] = 2

    return minutes if freshNum == 0 else -1



    
grid = [[2,1,1],[0,1,1],[1,0,1]]
print(orangesRotting(grid))





