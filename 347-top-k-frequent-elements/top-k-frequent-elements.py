class Solution:
    def topKFrequent(self, nums, k):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        return sorted(freq, key=freq.get, reverse=True)[:k]
        