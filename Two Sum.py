class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_dict = dict()
        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in complement_dict:
                return [complement_dict[compl], i]
            else:
                complement_dict[nums[i]] = i