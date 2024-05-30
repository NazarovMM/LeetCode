class Solution:
    def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
        output = []
        for word in words:
            split_word = word.split(separator)
            for j in split_word:
                if j != "":
                    output.append(j)
        return output


words = ["one.two.three", "four.five", "six"]
separator = "."

solution = Solution()
result = solution.splitWordsBySeparator(words, separator)
print(result)
