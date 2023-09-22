class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        number_arr = []
        num = int()
        while x != 0:
            num = x % 10
            number_arr.append(num)
            x = x // 10
        lower_ptr = 0
        upper_ptr = len(number_arr) - 1
        while upper_ptr > lower_ptr:
            if number_arr[upper_ptr] != number_arr[lower_ptr]:
                return False
            upper_ptr -= 1
            lower_ptr += 1
        return True