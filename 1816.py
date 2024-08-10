class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        return " ".join(s[:k])


s = "Hello how are you Contestant"
k = 4
solution = Solution()
result = solution.truncateSentence(s, k)
print(result)
