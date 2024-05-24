class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        output = ""
        for i in range(len(digits)):
            output += str(digits[i])
        output = int(output) + 1
        return (list([int(x) for x in str(output)]))


digits = [1, 2, 3]
solution = Solution()
result = solution.plusOne(digits)
print(result)
