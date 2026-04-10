class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        rows, cols = len(image), len(image[0])

        if image[sr][sc] == color:
            return image
        
        def dfs(i, j, org):
            if i < 0 or j < 0 or i >= rows or j >= cols or image[i][j] != org:
                return
            
            image[i][j] = color
            dfs(i + 1, j, org)
            dfs(i - 1, j, org)
            dfs(i, j + 1, org)
            dfs(i, j - 1, org)



        dfs(sr, sc, image[sr][sc])
        return image