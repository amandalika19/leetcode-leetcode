class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])

        def dfs(i, j, k):
            if k == len(word):
                return True
            
            if i < 0 or j < 0 or i >= rows or j >= cols or word[k] != board[i][j] or board[i][j] == '#':
                return False
            
            board[i][j] = '#'

            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)

            board[i][j] = word[k]
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        
        return False
        