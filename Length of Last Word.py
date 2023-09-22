class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_len = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " " and word_len != 0:
                return word_len
            if s[i] != " ":
                word_len += 1
        return word_len
            
                