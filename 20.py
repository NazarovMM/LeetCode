class Solution:
    def isValid(self, s: str) -> bool:
        buffer = []

        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                buffer.insert(0, ch)
            else:
                if buffer == []:
                    return False
                else:
                    if ch == ")":
                        if buffer[0] == "(":
                            buffer.pop(0)
                        else:
                            return False
                    elif ch == "}":
                        if buffer[0] == "{":
                            buffer.pop(0)
                        else:
                            return False
                    elif ch == "]":
                        if buffer[0] == "[":
                            buffer.pop(0)
                        else:
                            return False

        if buffer == []:
            return True
        else:
            return False


s = "){"
solution = Solution()
result = solution.isValid(s)
print(result)
