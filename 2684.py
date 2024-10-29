class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[0] * n for i in range(m)]
        visited = [[True] + [False] * (n - 1) for i in range(m)]

        for col in range(n - 1):
            for row in range(m):
                if not visited[row][col]:
                    continue
                
                if row - 1 >= 0 and grid[row][col] < grid[row - 1][col + 1]:
                    dp[row - 1][col + 1] = max(dp[row - 1][col + 1], dp[row][col] + 1)
                    visited[row - 1][col + 1] = True
                if grid[row][col] < grid[row][col + 1]:
                    dp[row][col + 1] = max(dp[row][col + 1], dp[row][col] + 1)
                    visited[row][col + 1] = True
                if row + 1 < m and grid[row][col] < grid[row + 1][col + 1]:
                    dp[row + 1][col + 1] = max(dp[row + 1][col + 1], dp[row][col] + 1)
                    visited[row + 1][col + 1] = True

        M = 0
        for row in dp:
            M = max(M, max(row))
        
        return M

        # dp = [[0] * m for i in range(n)]

        # for col in range(n - 1, 0, -1):
        #     for row in range(m):
        #         if row - 1 >= 0 and grid[row - 1][col - 1] < grid[row][col]:
        #             dp[col - 1][row - 1] = max(dp[col - 1][row - 1], dp[col][row] + 1)
        #         if grid[row][col - 1] < grid[row][col]:
        #             dp[col - 1][row] = max(dp[col - 1][row], dp[col][row] + 1)
        #         if row + 1 < m and grid[row + 1][col - 1] < grid[row][col]:
        #             dp[col - 1][row + 1] = max(dp[col - 1][row + 1], dp[col][row] + 1)

        # return max(dp[0])