class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            rem = n % 2
            n //= 2
            if rem ==1:
                res += 1
        return res