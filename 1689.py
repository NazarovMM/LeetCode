class Solution:
    def minPartitions(self, n: str) -> int:
        max_digit = max(n)
        return int(max_digit)


n = '273462083070182346'

solution = Solution()
result = solution.minPartitions(n)
print(result)
