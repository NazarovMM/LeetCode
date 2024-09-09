class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        total_ones = sum(nums)
        if total_ones == 0:
            return 0
        else:
            nums = nums + nums  # имитация кругового массива
            min_swaps = float('inf')
            current_ones = 0
            for i in range(2 * n):
                if i < total_ones:
                    current_ones += nums[i]
                else:
                    current_ones += nums[i] - nums[i - total_ones]
                if i >= total_ones - 1:
                    min_swaps = min(min_swaps, total_ones - current_ones)

        return min_swaps


nums = [0,0,0]

solution = Solution()
result = solution.minSwaps(nums)
print(result)
