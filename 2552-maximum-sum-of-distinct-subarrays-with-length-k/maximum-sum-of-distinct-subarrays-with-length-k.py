class Solution:
    def maximumSubarraySum(self, nums, k):
        seen = set()
        current_sum = 0
        max_sum = 0
        left = 0
        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            seen.add(nums[right])
            current_sum += nums[right]
            if right - left + 1 > k:
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            if right - left + 1 == k:
                max_sum = max(max_sum, current_sum)
        return max_sum