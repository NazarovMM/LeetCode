class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums = sorted(nums)
        counter = 0
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                counter += nums[i]-nums[i+1]+1
                nums[i+1] = nums[i+1] + (nums[i]-nums[i+1]) + 1
        return counter


nums = [3, 2, 1, 2, 1, 7]
solution = Solution()
result = solution.minIncrementForUnique(nums)
print(result)
