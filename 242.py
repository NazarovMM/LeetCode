from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


s = "rat"
t = "tara"
solution = Solution()
result = solution.isAnagram(s, t)
print(result)
