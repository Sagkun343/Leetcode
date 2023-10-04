class Solution:
    def fact(self, n: int) -> int:
        if n < 2:
            return 1
        else:
            return n*self.fact(n-1)
    def combination(self, n: int, r: int) -> int:
        return int(self.fact(n)/(self.fact(r)*self.fact(n-r)))
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_map = dict()
        res = 0
        for number in nums:
            if number in num_map:
                num_map[number] += 1
            else:
                num_map[number] = 1
        for number in num_map:
            if num_map[number] > 1:
                res += self.combination(num_map[number], 2)
        return res
        