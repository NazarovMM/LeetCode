class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        output = s.count(letter) / len(s) * 100
        return int(output)


s = "foobar"
letter = "o"
solution = Solution()
result = solution.percentageLetter(s, letter)
print(result)
