class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        new_nums = []
        for num in nums:
            new_num = ""
            for ch in str(num):
                new_num += str(mapping[int(ch)])
            new_nums.append(new_num)

        mapped_nums=list(zip(nums,new_nums))
        mapped_nums.sort(key=lambda x: int(x[1]))
        return [nums for nums, _ in mapped_nums]


mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
nums = [991, 338, 38]

solution = Solution()
result = solution.sortJumbled(mapping, nums)
print(result)
