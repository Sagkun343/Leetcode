class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        for num in nums:
            idx = abs(num)
            if nums[idx] < 0:
                return idx
            nums[idx] = -nums[idx]

        return length