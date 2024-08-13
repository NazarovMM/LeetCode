class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        current_point = 0
        highest_point = 0
        for ch in gain:
            current_point += ch
            if current_point > highest_point:
                highest_point = current_point
        return highest_point


gain = [-4,-3,-2,-1,4,3,2]
solution = Solution()
result = solution.largestAltitude(gain)
print(result)
