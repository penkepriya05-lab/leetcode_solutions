class Solution: 
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Minimum value from i to the end
        right_min = [0] * n
        right_min[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            right_min[i] = min(nums[i], right_min[i + 1])

        # Maximum value from 0 to i
        left_max = nums[0]

        for i in range(n):
            left_max = max(left_max, nums[i])

            if left_max - right_min[i] <= k:
                return i

        return -1