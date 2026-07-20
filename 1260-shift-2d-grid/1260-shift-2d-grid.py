class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        total = m*n
        k %= total
        ans = [[0]*n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                old_index = row*n + col
                new_index = (old_index + k) % total
                new_row = new_index // n
                new_col = new_index % n
                ans[new_row][new_col] = grid[row][col]
        
        return ans