class Solution:
    def addDigits(self, num: int) -> int:
        output = num
        while output//10 != 0:
            buff = str(output)
            output = 0
            for i in buff:
                output += int(i)
        return output


num = 38
solution = Solution()
result = solution.addDigits(num)
print(result)
