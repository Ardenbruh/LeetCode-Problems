class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fo = 0
        rotq = deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fo+=1
                elif grid[i][j] == 2:
                    rotq.appendleft((i,j,0))
        
        if not fo:
            return 0

        directions = {(1,0),(-1,0),(0,1),(0,-1)}

        while rotq:
            roi, roj, t = rotq.pop()
            for di, dj in directions:
                noi, noj = roi + di, roj + dj
                if -1<noi<m and -1<noj<n and grid[noi][noj]==1:
                    fo-=1
                    if not fo:
                        return t+1
                    grid[noi][noj] = 2
                    rotq.appendleft((noi,noj,t+1))
        return -1