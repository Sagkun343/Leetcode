class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == "[" or bracket == "(" or bracket == "{":
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                else:
                    last_char = stack[len(stack) - 1]
                if ord(bracket) == (ord(last_char) + 1) or ord(bracket) == (ord(last_char) + 2):
                    stack.pop(len(stack) - 1)
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False