class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_length = len(s)
        if s_length == 0:
            return True
        iterator = 0
        for k in range(len(t)):
            if s[iterator] == t[k]:
                iterator += 1
            if iterator == s_length:
                return True
        return False