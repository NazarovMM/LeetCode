class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        hash = {}
        for ch in arr:
            if ch not in hash:
                hash[ch] = 1
            else:
                hash[ch] += 1
        output = ''
        counter = 0
        for key in hash.keys():
            if hash[key] == 1:
                counter += 1
            if counter == k:
                output = key
                return output
        return output


arr = ["a", "b", "a"]
k = 3

solution = Solution()
result = solution.kthDistinct(arr, k)
print(result)
