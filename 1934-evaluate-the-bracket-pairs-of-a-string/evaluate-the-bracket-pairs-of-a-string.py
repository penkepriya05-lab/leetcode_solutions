class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        mp = dict(knowledge)
        result = ""
        i = 0
        while i < len(s):
            if s[i] == '(':
                j = s.index(')', i)
                key = s[i + 1:j]
                result += mp.get(key, '?')
                i = j + 1
            else:
                result += s[i]
                i += 1
        return result        