class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        flag = False
        if "-" in x_str:
            flag = True
            x_str = x_str.removeprefix('-')
        x_str = x_str[::-1]
        if flag:
            x_str = (-1)*int(x_str)
        else:
            x_str = int(x_str)
        if ((-2)**31) <= x_str <= (2**31-1):
            return x_str
        else:
            return 0


solution = Solution()
num = 1534236469
result = solution.reverse(num)
print(result)
