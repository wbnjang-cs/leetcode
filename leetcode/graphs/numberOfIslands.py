
from collections import deque

def numIslands(grid):
    seen = set()
    stack = deque()

    hor = len(grid[0])
    ver = len(grid)

    islandNum = 0

    for i in range(ver):
        for j in range(hor):


            if (i,j) in seen:
   
                continue

            elif grid[i][j] == "0":
        
                seen.add((i,j))
            
            elif grid[i][j] == "1":
       

                stack.append((i,j))

                while stack:
                    for k in range(len(stack)):
               
                        v, h = stack.pop()
                        if h != hor-1 and (v, h+1) not in seen and grid[v][h+1] == "1":
                            stack.append((v, h+1))
                            seen.add((v, h+1))

                        
                        if h != 0 and (v, h-1) not in seen and grid[v][h-1] == "1":
                            stack.append((v, h-1))
                            seen.add((v, h-1))

                        if v != 0 and (v-1, h) not in seen and grid[v-1][h] == "1":
                            stack.append((v-1, h))
                            seen.add((v-1,h))
                        
                        if v != ver-1 and (v+1,h) not in seen and grid[v+1][h] == "1":
                            stack.append((v+1, h))
                            seen.add((v+1,h))
                        

                islandNum +=1

            
    
    return islandNum

def numIslandsAnswer(grid):
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    seen = set()
    islandNum = 0

    def dfs(r,c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0" or (r,c) in seen:
            return
        
        seen.add((r,c))

        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)

    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in seen:
                islandNum +=1
                dfs(r,c)
    
    return islandNum



