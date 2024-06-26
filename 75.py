class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter_list = [0, 0, 0]
        for i in range(len(nums)):
            if nums[i] == 0:
                counter_list[0] += 1
            elif nums[i] == 1:
                counter_list[1] += 1
            else:
                counter_list[2] += 1
        j = 0
        for i in range(3):
            while counter_list[i] > 0:
                nums[j] = i
                j += 1
                counter_list[i] -= 1
        return nums


nums = [2, 0, 2, 1, 1, 0]
solution = Solution()
result = solution.sortColors(nums)
print(result)
