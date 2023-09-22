class Solution:
    def minDeletions(self, s: str) -> int:
        mydict = dict()
        newdict = dict()
        for i in s:
            if i in mydict:
                mydict[i] += 1
            else:
                mydict[i] = 1
        val = 0
        for key in mydict:
            temp = mydict[key]
            while (temp in newdict):
                val += 1
                temp -= 1
                if temp == 0:
                    break
            newdict[temp] = key
        return val
