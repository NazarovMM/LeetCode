class Solution:
    def maxArea(self, height: list[int]) -> int:
        maximum_area = 0
        left = 0
        right = len(height)-1

        while left < right:
            h = min(height[left], height[right])
            w = right-left
            area = h*w
            
            maximum_area = max(maximum_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maximum_area


height = [2, 3, 4, 5, 18, 17, 6]

solution = Solution()
result = solution.maxArea(height)
print(result)
