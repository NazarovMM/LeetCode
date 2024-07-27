class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i]+nums[j] == target and i != j:
                    return [i, j]


class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash = {}
        for k, value in enumerate(nums):
            if target-value in hash:
                return [hash[target-value], k]
            hash[value] = k


nums = [2, 11, 5, 5]
target = 10

solution = Solution2()
result = solution.twoSum(nums, target)
print(result)
