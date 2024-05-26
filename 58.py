class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        num = list([x for x in s.split(" ")])
        for x in range(len(num), 0, -1):
            if num[x-1] != "":
                return len(num[x-1])


text = "a aa"
solution = Solution()
result = solution.lengthOfLastWord(text)
print(result)
