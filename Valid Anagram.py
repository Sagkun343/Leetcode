class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = dict()
        dict_t = dict()
        for i in s:
            if i in dict_s:
                dict_s[i] += 1
            else:
                dict_s[i] = 1
        for i in t:
            if i in dict_t:
                dict_t[i] += 1
            else:
                dict_t[i] = 1

        if dict_s == dict_t:
            return True
        else:
            return False
            