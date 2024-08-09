class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i):
                nums[i] += nums[j]
        return nums


nums = [3, 1, 2, 10, 1]

solution = Solution()
result = solution.runningSum(nums)
print(result)
