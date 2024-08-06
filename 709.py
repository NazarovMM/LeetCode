class Solution:
    def toLowerCase(self, s: str) -> str:
        output = ""
        for ch in s:
            ascii_code = ord(ch)
            if ascii_code >= 65 and ascii_code <= 90:
                output += chr(ascii_code + 32)
            else:
                output += ch
        return output


n = 'hH'
solution = Solution()
result = solution.toLowerCase(n)
print(result)
