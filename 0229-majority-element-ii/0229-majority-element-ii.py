class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_1 = count_2 = candidate_1 = 0
        candidate_2 = 0
        res = []
        for num in nums:
            if num == candidate_1:
                count_1 += 1
            elif num == candidate_2:
                count_2 += 1
            elif count_1 == 0:
                candidate_1 = num
                count_1 = 1
            elif count_2 == 0:
                candidate_2 = num
                count_2 = 1
            else:
                count_1 -= 1
                count_2 -= 1
        count_1 = count_2 = 0
        for num in nums:
            if num == candidate_1:
                count_1 += 1
            elif num == candidate_2:
                count_2 += 1
        if (count_1 > len(nums) //3):
            res.append(candidate_1)
        if (count_2 > len(nums) // 3) and candidate_2 != candidate_1:
            res.append(candidate_2)
        return res



