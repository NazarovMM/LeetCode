class Solution:
    def countSegments(self, s: str) -> int:
        '''if len(s) == 0 or s == " ":
            return 0'''
        output = 0
        s = s.split(" ")
        print(s)
        for ch in s:
            if ch != '':
                output += 1
        return output


s = " a"

solution = Solution()
result = solution.countSegments(s)
print(result)
