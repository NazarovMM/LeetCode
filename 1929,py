class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = list(x for x in range(len(nums)*2))
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[len(nums)+i] = nums[i]
        return ans


nums = [1, 3, 2, 1]

solution = Solution()
result = solution.getConcatenation(nums)
print(result)
