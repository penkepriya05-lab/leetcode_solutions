from typing import List
from functools import lru_cache

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # Total path length must be even
        if (m + n - 1) % 2 == 1:
            return False

        # Start must be '('
        if grid[0][0] == ')':
            return False

        # End must be ')'
        if grid[m - 1][n - 1] == '(':
            return False

        @lru_cache(None)
        def dfs(i, j, balance):
            # Balance can never be negative
            if balance < 0:
                return False

            # Number of cells still available including current position
            remaining = (m - 1 - i) + (n - 1 - j)

            # We need enough ')' to reduce balance to 0
            if balance > remaining:
                return False

            # Reached destination
            if i == m - 1 and j == n - 1:
                return balance == 0

            # Move down
            if i + 1 < m:
                new_balance = balance + (1 if grid[i + 1][j] == '(' else -1)

                if dfs(i + 1, j, new_balance):
                    return True

            # Move right
            if j + 1 < n:
                new_balance = balance + (1 if grid[i][j + 1] == '(' else -1)

                if dfs(i, j + 1, new_balance):
                    return True

            return False

        return dfs(0, 0, 1)