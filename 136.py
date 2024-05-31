class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        output = 0
        for i in nums:
            output = output ^ i
        return output


nums = [1]
solution = Solution()
result = solution.singleNumber(nums)
print(result)
