class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        sum_elements = 0
        sum_digits = 0
        for num in nums:
            sum_elements += num
            for ch in str(num):
                sum_digits += int(ch)
        return abs(sum_elements-sum_digits)


nums = [1, 15, 6, 3]

solution = Solution()
result = solution.differenceOfSum(nums)
print(result)
