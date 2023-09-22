class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_val = 0
        for i in nums:
            xor_val ^= i
        return xor_val