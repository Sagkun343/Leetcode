class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        prn = []
        operators = {"+", "-", "/", "*"}
        res = 0
        index = 0
        for token in tokens:
            if token in operators:
                if token == "+":
                    res += int(prn[index-2]) + int(prn[index-1])
                if token == "-":
                    res += int(prn[index-2]) - int(prn[index-1])
                if token == "*":
                    res += int(prn[index-2]) * int(prn[index-1])
                if token == "/":
                    res += int(prn[index-2]) / int(prn[index-1])
                prn.pop(index - 1)
                prn.pop(index - 2)
                index -= 1
                prn.append(res)
                res = 0
            else:
                index += 1
                prn.append(token)
        return int(prn[0])