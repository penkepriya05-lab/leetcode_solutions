class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=[]
        s2=[]
        for ch in s:
            if ch!="#":
                s1.append(ch)
            else:
                if s1:
                    s1.pop()
        for ch in t:
            if ch!="#":
                s2.append(ch)
            else:
                if s2:
                    s2.pop()
        if s1==s2:
            return True
        else:
            return False