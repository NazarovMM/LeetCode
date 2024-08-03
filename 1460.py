class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        return sorted(target)==sorted(arr)


target = [3,7,9]
arr = [3,7,11]
solution = Solution()
result = solution.canBeEqual(target, arr)
print(result)
