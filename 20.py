class Solution:
    def isValid(self, s: str) -> bool:
        flag = True
        while s != "":
            if s[0] == "(" and ")" in s:
                s = s[2:]
            elif s[0] == "[" and "]" in s:
                s = s[2:]
            elif s[0] == "{" and "}" in s:
                s = s[2:]
            else:
                flag = False
                break
        if flag:
            return True
        else:
            return False


s = "(]"
solution = Solution()
result = solution.isValid(s)
print(result)