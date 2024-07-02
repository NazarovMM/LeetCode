import collections


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        ans = []
        count = collections.Counter(nums1)
        for num in nums2:
            if count[num] > 0:
                ans.append(num)
                count[num] -= 1
        return ans


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

solution = Solution()
result = solution.intersect(nums1, nums2)
print(result)
