class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        rowsC = [0] * rows
        colsC = [0] * cols

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    rowsC[r] += 1
                    colsC[c] += 1
        
        servers = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and max(rowsC[r], colsC[c]) > 1:
                    servers += 1
        
        return servers