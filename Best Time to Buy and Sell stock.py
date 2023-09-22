class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_number = prices[0]
        difference = 0
        for i in prices:
            if i < lowest_number:
                lowest_number = i
            else:
                if difference < (i - lowest_number):
                    difference = i - lowest_number
        return difference