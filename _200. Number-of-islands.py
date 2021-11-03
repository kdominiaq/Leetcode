class Solution:
    def mark_current_island(self, grid, r, c, max_r, max_c):
        
        if r < 0 or r > max_r - 1 or c < 0 or c > max_c -1:
            return None
        print(r,c)
        if grid[r][c] != '1': 
            return None 
  

        grid[r][c] = '2'

        self.mark_current_island(grid, r + 1, c, max_r, max_c)
        self.mark_current_island(grid, r - 1, c, max_r, max_c)
        self.mark_current_island(grid, r, c + 1, max_r, max_c)
        self.mark_current_island(grid, r, c - 1, max_r, max_c)

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)      # row
        n = len(grid[0])   # col
        
        nb_of_islands = 0
        
        if m <= 0:
            return 0
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    self.mark_current_island(grid, row, col, m, n)
                    nb_of_islands += 1
       
        return nb_of_islands
                    
                
