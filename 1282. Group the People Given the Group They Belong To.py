class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        mydict = dict()
        output_arr = []
        for i in range(len(groupSizes)):
            if groupSizes[i] in mydict:
                mydict[groupSizes[i]] += [i]
            else:
                mydict[groupSizes[i]] = [i]
        for key in mydict:
            iter = int(len(mydict[key]) / key)
            for n in range(iter):
                output_arr.append(mydict[key][n*key:(((n+1)*key))])
        return output_arr