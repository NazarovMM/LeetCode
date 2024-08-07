class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        s = [ch[::-1] for ch in s]
        return "".join(ch+" " for ch in s).removesuffix(" ")

s = "Let's take LeetCode contest"
solution = Solution()
result = solution.reverseWords(s)
print(result)