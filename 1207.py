class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        hash = {}
        for num in arr:
            if num not in hash:
                hash[num] = 1
            else:
                hash[num] += 1
        set_hash = set(hash.values())
        if len(set_hash) == len(hash.values()):
            return True
        else:
            return False


arr = [1, 2, 2, 1, 1, 3, 3]

solution = Solution()
result = solution.uniqueOccurrences(arr)
print(result)
