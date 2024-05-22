from itertools import combinations


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        values = []
        output = []
        for i in range(len(nums)+1):
            values = list(combinations(nums, i))
            output += [list(x) for x in values]
        return output

solution = Solution()
nums = [1, 2, 3]
result = solution.subsets(nums)
print(result)
