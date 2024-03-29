class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0,0 
        ROWS, COLS = len(grid), len(grid[0])
        
        #for loof going through all the points in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    fresh+=1 #calculation fresh oranges
                if grid[r][c]==2:
                    q.append([r,c]) #appending rotten oranges
        
        #all the four directions 
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh>0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    row = r+dr
                    col = c+dc
                    # if in bounds and fresh, make rotten
                    if (row < 0 or row == ROWS or col<0 or col == COLS or grid[row][col]!=1):
                        continue
                    grid[row][col]=2
                    q.append([row,col])
                    fresh-=1
            time+=1
        return time if fresh ==0 else -1
        
        