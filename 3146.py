class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_hash = {}
        t_hash = {}
        for i in range(len(s)):
            s_hash[s[i]] = i
            t_hash[t[i]] = i
        output = 0
        for keys in s_hash.keys():
            output += abs(s_hash[keys]-t_hash[keys])
        return output


s = "abcde"
t = "abcde"

solution = Solution()
result = solution.findPermutationDifference(s, t)
print(result)
