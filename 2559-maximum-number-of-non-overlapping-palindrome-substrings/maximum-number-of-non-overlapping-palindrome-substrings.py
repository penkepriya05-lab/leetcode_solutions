class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        palindrome = [bytearray(n) for _ in range(n)]
        for i in range(n - 1, -1, -1):
            palindrome[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j] and (j - i == 1 or palindrome[i + 1][j - 1]):
                    palindrome[i][j] = 1
        dp = [0] * (n + 1)
        for r in range(n):
            dp[r + 1] = dp[r]
            for l in range(r + 1):
                if r - l + 1 >= k and palindrome[l][r]:
                    dp[r + 1] = max(dp[r + 1], dp[l] + 1)
        return dp[n]