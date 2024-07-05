class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        buff = ""
        output = []
        for ch in s:
            if ch not in buff:
                buff += ch
            else:
                output.append(buff)
                for x in buff:
                    if x == ch:
                        search = buff.find(x)
                        buff_new = buff[search+1:]
                buff_new += ch
                buff = buff_new
        output.append(buff)
        print(output)
        return max(len(x) for x in output)


s = "dvdf"

solution = Solution()
result = solution.lengthOfLongestSubstring(s)
print(result)
