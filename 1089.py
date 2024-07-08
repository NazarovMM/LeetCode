class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0
        for _ in range(n):
            if i < n:
                if arr[i] == 0:
                    arr.insert(i+1, 0)
                    arr.pop()
                    i += 2
                else:
                    i += 1
        return arr


arr = [1, 0, 2, 3, 0, 4, 5, 0]
solution = Solution()
result = solution.duplicateZeros(arr)
print(result)
