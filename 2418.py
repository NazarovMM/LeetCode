class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        buff = list(zip(names, heights))
        res = sorted(buff, key=lambda x: x[1], reverse=True)
        x, y = zip(*res)
        return x


names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]
# Output: ["Mary","Emma","John"]
solution = Solution()
result = solution.sortPeople(names, heights)
print(result)
