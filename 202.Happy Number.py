class Solution:
    def matrix(self, num: int, num_set: set):
      if num == 1:
        return True
      digits = list(str(num))
      accumulator = 0
      for num in digits:
        accumulator += pow(int(num), 2)
      if accumulator in num_set:
        return False
      else:
        num_set.add(accumulator)
        return self.matrix(accumulator, num_set)
      
    def isHappy(self, n: int) -> bool:
      return self.matrix(n, set())