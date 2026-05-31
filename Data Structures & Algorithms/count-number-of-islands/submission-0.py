class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(row, col):
            if row < 0 or row > len(grid) - 1:
                return
            if col < 0 or col > len(grid[0]) - 1:
                return
            if grid[row][col] != '1':
                return
            
            grid[row][col] = '0'

            bfs(row - 1, col)
            bfs(row, col - 1)
            bfs(row + 1, col)
            bfs(row, col + 1)
                
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1
                    bfs(i, j)
        
        return count


        


        
                