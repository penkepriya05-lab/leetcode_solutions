class Solution:
    def checkSubarraySum(self, nums, k):
        r_map = {0: -1}
        prefix = 0
        for i in range (len(nums)):
            prefix += nums[i]
            rem = prefix % k
            if rem in r_map:
                if i - r_map[rem] >= 2:
                    return True
            else:
                r_map[rem] = i
        return False
        