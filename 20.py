class Solution:
    def isValid(self, s: str) -> bool:
        krygl = 0
        kvadr = 0
        figur = 0
        for i in s:
            if i == "(":
                krygl+=1
            elif i ==")":
                krygl-=1
            elif i=="[":
                kvadr+=1
            elif i=="]":
                kvadr-=1
            elif i=="{":
                figur+=1
            else:
                figur-=1
        if krygl == kvadr == figur == 0:
            return True
        else:
            return False

s = "([)]"
solution = Solution()
result = solution.isValid(s)
print(result)
