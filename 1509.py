class Solution:
    def minDifference(self, nums: list[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        return min(
            nums[-1] - nums[3],  # меняем три наименьших
            nums[-2] - nums[2],  # меняем два наименьших и один наибольший
            nums[-3] - nums[1],  # меняем один наименьший и два наибольших
            nums[-4] - nums[0]   # меняем три наибольших
        )


nums = [53, 60, 100, 85, 16, 68, 64, 31, 37, 78]

solution = Solution()
result = solution.minDifference(nums)
print(result)
