class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_count = float("-inf")
        for sentence in sentences:
            sentence = sentence.split(" ")
            if len(sentence) > max_count:
                max_count = len(sentence)
        return max_count


sentences = ["please wait", "continue to fight", "continue to win"]

solution = Solution()
result = solution.mostWordsFound(sentences)
print(result)
