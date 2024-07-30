class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        output = []
        for i in range(len(words)):
            if words[i].count(x) != 0:
                output.append(i)
        return output


words = ["abc", "bcd", "aaaa", "cbc"]
x = "z"

solution = Solution()
result = solution.findWordsContaining(words, x)
print(result)
