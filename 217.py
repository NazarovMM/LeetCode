class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        num_set = set()
        for n in nums:
            if n in num_set:
                return True
            num_set.add(n)
        return False


nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
solution = Solution()
result = solution.containsDuplicate(nums)
print(result)
