class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        oldColor = image[sr][sc]
        if oldColor == newColor:  
            return image

        rows, cols = len(image), len(image[0])

        def dfs(r, c):
            
            if not (0 <= r < rows and 0 <= c < cols and image[r][c] == oldColor):
                return image

            image[r][c] = newColor  

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image
