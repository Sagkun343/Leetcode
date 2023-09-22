class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower_point = 0
        upper_point = len(nums) - 1
        while upper_point >=  lower_point:
            midpoint = ((upper_point + lower_point) // 2)
            if target == nums[midpoint]:
                return midpoint
            if target > nums[midpoint]:
                lower_point = midpoint + 1
            else:
                upper_point = midpoint - 1
        return -1