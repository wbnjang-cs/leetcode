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
    hor = len(grid[0])
    ver = len(grid)
    numFresh = 0

    for i in range(ver):
        for j in range(hor):
            if grid[i][j] == 1:
                numFresh +=1
            if grid[i][j] == 2:
                q.append((i,j))
    
    if numFresh == 0:
        return 0
    dirs = [(1,0), (0,1), (-1,0), (0,-1)]

    while 1 and numFresh > 0:
        for orange in range(len(q)):
            r,c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ver and 0 <= nc < hor and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    numFresh -=1
                    q.append((nr,nc))
        
        minutes +=1
    
    return minutes if numFresh == 0 else -1

    
grid = [[2,1,1],[0,1,1],[1,0,1]]
print(orangesRotting(grid))





