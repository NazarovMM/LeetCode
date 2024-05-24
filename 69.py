class Solution:
    def mySqrt(self, x: int) -> int:
        output = 0
        for i in range(int(x/2)+2):
            if i*i <= x:
                output = i
            else:
                break
        return output

solution = Solution()
x = 9
result = solution.mySqrt(x)
print(result)
