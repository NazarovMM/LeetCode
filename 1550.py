class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        chk = 0
        for i in range(len(arr)):
            if arr[i] % 2 != 0:
                chk += 1
            else:
                chk = 0
            if chk == 3:
                return True
        return False


# arr = [2, 6, 4, 1]
arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
solution = Solution()
result = solution.threeConsecutiveOdds(arr)
print(result)
