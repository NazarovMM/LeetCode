class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        counter = 0
        for i in range(len(nums) - 1):
            n = i
            for j in range(n + 1, len(nums)):
                if nums[i] == nums[j]:
                    counter += 1
        return counter


nums = [1,2,3]

solution = Solution()
result = solution.numIdenticalPairs(nums)
print(result)
