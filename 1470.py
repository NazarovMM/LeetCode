class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        output = []
        for i in range(n):
            output.append(nums[i])
            output.append(nums[n+i])
        return output


nums = [2, 5, 1, 3, 4, 7]
n = 3

solution = Solution()
result = solution.shuffle(nums, n)
print(result)
