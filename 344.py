class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        return s


s = ["H","a","n","n","a","h"]
solution = Solution()
result = solution.reverseString(s)
print(result)
