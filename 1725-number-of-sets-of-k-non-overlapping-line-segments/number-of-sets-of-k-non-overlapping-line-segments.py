class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        numerator = 1
        denominator = 1
        for i in range(1, 2 * k + 1):
            numerator *= n + k - i
            denominator *= i
        return (numerator // denominator) % MOD