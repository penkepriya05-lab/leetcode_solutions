class Solution:
    def frequencySort(self, s):
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        result = ""

        for ch in sorted(freq, key=freq.get, reverse=True):
            result += ch * freq[ch]

        return result