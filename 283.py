class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero_found_at = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_found_at] = nums[i]
                last_non_zero_found_at += 1
        for i in range(last_non_zero_found_at, len(nums)):
            nums[i] = 0
        return nums


nums = [0, 1, 0, 3, 12]

solution = Solution()
result = solution.moveZeroes(nums)
print(result)
