class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        buff = ''
        for ch in word1:
            buff += ch
        word1.clear()
        word1.append(buff)
        buff = ''
        for ch in word2:
            buff += ch
        word2.clear()
        word2.append(buff)
        return word1 == word2


word1  = ["abc", "d", "defg"]
word2 = ["abcddefg"]

solution = Solution()
result = solution.arrayStringsAreEqual(word1, word2)
print(result)
