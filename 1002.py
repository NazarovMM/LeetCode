class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        output = []
        for ch in words[0]:
            counter = 1  # чтобы учитывать букву из 1 слова
            for i in range(1, len(words)):
                if ch in words[i]:
                    counter += 1
                    words[i] = words[i].replace(ch, "_", 1)
                    pass
                if counter == len(words):
                    output.append(ch)
        return output


words = ["cool", "lock", "cook"]
solution = Solution()
result = solution.commonChars(words)
print(result)
