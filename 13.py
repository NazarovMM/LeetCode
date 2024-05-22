class Solution:
    def romanToInt(self, s: str) -> int:
        rim = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        lenth = len(s)
        output = 0
        while lenth > 0:
            if lenth == 1:
                output += rim.get(s[0])
                lenth = 0
            elif rim.get(s[0]) < rim.get(s[1]):
                if s[0] == 'I':
                    if s[1] == 'V':
                        output += 4
                    elif s[1] == 'X':
                        output += 9
                elif s[0] == 'X':
                    if s[1] == 'L':
                        output += 40
                    elif s[1] == 'C':
                        output += 90
                elif s[0] == 'C':
                    if s[1] == 'D':
                        output += 400
                    elif s[1] == 'M':
                        output += 900
                lenth -= 2
                s = s[2:]
            else:
                output += rim.get(s[0])
                s = s[1:]
                lenth -= 1
        return output


solution = Solution()
result = solution.romanToInt("MCMXCIV")
print(result)
