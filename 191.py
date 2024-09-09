class Solution:
    def hammingWeight(self, n: int) -> int:
        output = bin(n)[2:]
        count = output.count('1')
        return count


n = 11

solution = Solution()
result = solution.hammingWeight(n)
print(result)
