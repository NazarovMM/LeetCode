class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        output = list(s)
        for i in range(len(indices)):
            output[indices[i]] = s[i]
        return "".join(output)


s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]

solution = Solution()
result = solution.restoreString(s, indices)
print(result)
