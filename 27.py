class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        counter = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[counter] = nums[i]
                counter += 1
        return counter


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
solution = Solution()
result = solution.removeElement(nums, val)
print(result)
