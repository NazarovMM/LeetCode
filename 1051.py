class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        s_heights = sorted(heights)
        counter = 0
        for i in range(len(heights)):
            if s_heights[i] != heights[i]:
                counter += 1
        return counter


heights = [1,2,3,4,5]
solution = Solution()
result = solution.heightChecker(heights)
print(result)
