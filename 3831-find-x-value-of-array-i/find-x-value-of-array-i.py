class Solution:
    def resultArray(self, nums, k):
        ans = [0] * k
        dp = [0] * k
        for num in nums:
            new_dp = [0] * k
            new_dp[num % k] += 1
            for r in range(k):
                if dp[r]:
                    new_r = (r * (num % k)) % k
                    new_dp[new_r] += dp[r]
            dp = new_dp
            for r in range(k):
                ans[r] += dp[r]
        return ans