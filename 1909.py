class Solution:
    def canBeIncreasing(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            nums_mod = nums.copy()
            nums_mod.pop(i)
            flag = 0
            if len(nums_mod) == 1:
                return True
            for j in range(len(nums_mod)-1):
                if nums_mod[j] < nums_mod[j+1]:
                    flag += 1
                if flag == len(nums_mod)-1:
                    return True
        return False


nums = [512, 867, 904, 997, 403]

solution = Solution()
result = solution.canBeIncreasing(nums)
print(result)
# позже оптимизировать
