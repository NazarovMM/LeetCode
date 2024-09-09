class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) > 1:

            r = len(nums) // 2
            L = nums[:r]
            M = nums[r:]

            Solution().sortArray(L)
            Solution().sortArray(M)

            i = j = k = 0

            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = M[j]
                    j += 1
                k += 1

            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1

            while j < len(M):
                nums[k] = M[j]
                j += 1
                k += 1
        return nums