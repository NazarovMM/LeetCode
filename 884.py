class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        s1 = s1.split(' ')
        s2 = s2.split(' ')
        s = s1+s2
        buff = {}
        for word in s:
            if word in buff:
                buff[word] += 1
            else:
                buff[word] = 1
        return (list(word for word in buff if buff[word] == 1))


s1 = "apple apple"
s2 = "sour"

solution = Solution()
result = solution.uncommonFromSentences(s1, s2)
print(result)
