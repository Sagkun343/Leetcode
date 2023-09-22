class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        occurance = 0
        for number in range(len(nums)):
            if nums[number] != val:
                nums[occurance] = nums[number]
                occurance += 1
        return occurance