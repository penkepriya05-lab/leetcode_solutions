from typing import List
from functools import lru_cache

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        if (m + n - 1) % 2 == 1:
            return False
        if grid[0][0] == ')':
            return False
        if grid[m - 1][n - 1] == '(':
            return False
        @lru_cache(None)
        def dfs(i, j, balance):
            if balance < 0:
                return False
            remaining = (m - 1 - i) + (n - 1 - j)
            if balance > remaining:
                return False
            if i == m - 1 and j == n - 1:
                return balance == 0
            if i + 1 < m:
                new_balance = balance + (1 if grid[i + 1][j] == '(' else -1)
                if dfs(i + 1, j, new_balance):
                    return True
            if j + 1 < n:
                new_balance = balance + (1 if grid[i][j + 1] == '(' else -1)
                if dfs(i, j + 1, new_balance):
                    return True
            return False
        return dfs(0, 0, 1)