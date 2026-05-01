class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])
        v = set()

        def dfs(i, j, k):
            if k == len(word):
                return True

            if i < 0 or j < 0 or i >= rows or j >= cols or word[k] != board[i][j] or board[i][j] == '#':
                return False
            
            board[i][j] = '#'
           
            res = (dfs(i + 1, j, k + 1) or 
            dfs(i - 1, j, k + 1) or 
            dfs(i, j + 1, k + 1) or
            dfs(i, j - 1, k + 1))

            board[i][j] = word[k]
            return res
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False
