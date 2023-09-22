class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort() # sort the numbers in ascending order

        l, r = 0, 1 # setting up two pointers

        while(r<len(nums)):
            if nums[l] == nums[r]: # checking if both same
                return True
            else:
                l += 1 # move the pointers one step ahead
                r += 1 # ^^

        return False