class Solution:
    def isPalindrome(self, x: int) -> bool:
        flag = False
        out = str(x)
        if len(out) % 2 == 0:
            for i in range(int(len(out) / 2)):
                if out[i] == out[len(out) - 1 - i]:
                    flag = True
                else:
                    flag = False
                    break
        else:
            if len(out) == 1:
                flag = True
            else:
                for i in range(int(len(out) / 2)):
                    if out[i] == out[len(out) - 1 - i]:
                        flag = True
                    else:
                        flag = False
                        break
        if flag:
            return True
        else:
            return False


solution = Solution()
y=10
result = solution.isPalindrome(y)
print(result)
