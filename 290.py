class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        hash = {}
        buff = []
        if len(s) != len(pattern):
            return False
        else:
            for i in range(len(pattern)):
                if s[i] not in buff:
                    buff.append(s[i])
                if pattern[i] not in hash:
                    hash[pattern[i]] = s[i]
                else:
                    if hash[pattern[i]] == s[i]:
                        pass
                    else:
                        return False
        return (len(hash) == len(buff))


pattern = "aaa"
s = "aa aa aa aa"
solution = Solution()
result = solution.wordPattern(pattern, s)
print(result)
