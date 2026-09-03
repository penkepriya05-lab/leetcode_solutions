class Solution:
    def uniformArray(self, nums1):
        min_odd = float('inf')
        for x in nums1:
            if x % 2 == 1:
                min_odd = min(min_odd, x)
        for x in nums1:
            if x % 2 == 0 and min_odd != float('inf') and x < min_odd:
                return False
        return True