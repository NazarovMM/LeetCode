class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l_counter = 0
        output = 0
        for ch in s:
            if ch == 'L':
                l_counter += 1
            if ch == "R":
                l_counter -= 1
            if l_counter == 0:
                output += 1
        return output


s = "RLRRLLRLRL"

solution = Solution()
result = solution.balancedStringSplit(s)
print(result)
