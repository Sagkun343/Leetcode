class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        for i in range(len(strs)):
            word_list = [0]*26
            for k in range(len(strs[i])):
                word_val = ord(strs[i][k]) - 97
                word_list[word_val] += 1
            tup = tuple(word_list)
            if tup in hashmap:
                hashmap[tup].append(strs[i])
            else:
                hashmap[tup] = [strs[i]]
        word_list = []
        return list(hashmap.values())
