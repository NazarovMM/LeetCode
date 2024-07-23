class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        dictionary = {}
        for i in range(len(nums)):
            if nums[i] not in dictionary.keys():
                dictionary.setdefault(nums[i], nums.count(nums[i]))
            else:
                continue
        sorted_dictionary = sorted(
            dictionary.items(), key=lambda item: item[1])
        output = list()
        for i in range(len(sorted_dictionary)):
            for j in range(sorted_dictionary[i][1]):
                output.append(sorted_dictionary[i][0])
        return output


nums = [2,3,1,3,2]
solution = Solution()
result = solution.frequencySort(nums)
print(result)
