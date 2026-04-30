class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        rowsc = [0] * rows
        colsc = [0] * cols


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    rowsc[i] += 1
                    colsc[j] += 1
        
        servers = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and max(rowsc[i], colsc[j]) > 1:
                    servers += 1
        
        return servers