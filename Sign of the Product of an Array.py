class Solution:
    def arraySign(self, nums: List[int]) -> int:
        flag = True
        val = 0
        for i in nums:
            if i > val:
              continue
            elif i < val:
                flag = not(flag)
            else:
                return 0
        if flag is True:
            return 1
        else:
            return -1