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


class Solution1:
    def isValid(self, s: str) -> bool:
        buffer = []
        for ch in s:
            if ch in "({[":
                buffer.append(ch)
            else:
                if buffer:
                    last_ch = buffer.pop()
                    if last_ch == "(" and ch == ")":
                        continue
                    if last_ch == "{" and ch == "}":
                        continue
                    if last_ch == "[" and ch == "]":
                        continue
                return False
        return len(buffer) == 0


s = "()"
solution = Solution1()
result = solution.isValid(s)
print(result)
