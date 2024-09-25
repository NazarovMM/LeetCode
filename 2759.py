class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        output = num
        for _ in range(1, t + 1):
            output += 2
        return output


num = -5
t = 3

solution = Solution()
result = solution.theMaximumAchievableX(num, t)
print(result)
