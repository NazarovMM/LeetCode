class Solution:
    def addBinary(self, a: str, b: str) -> str:
        output = ""
        a = a[::-1]
        b = b[::-1]
        if len(a) >= len(b):
            n = len(a)
        else:
            n = len(b)

        buff = 0
        for i in range(n):
            if i < len(a):
                vol1 = a[i]
            else:
                vol1 = '0'

            if i < len(b):
                vol2 = b[i]
            else:
                vol2 = '0'

            if vol1 == '1' and vol2 == '1' and buff == 0:
                output += '0'
                buff = 1
            elif vol1 == '1' and vol2 == '1' and buff == 1:
                output += '1'
                buff = 1
            elif (vol1 == '1' or vol2 == '1') and buff == 1:
                output += '0'
                buff = 1
            elif (vol1 == '1' or vol2 == '1') and buff == 0:
                output += '1'
            elif vol1 == '0' and vol2 == '0' and buff == 1:
                output += '1'
                buff = 0
            else:
                output += '0'
        if buff:
            output += '1'
        return output[::-1]


a = "1111"
b = "1111"

solution = Solution()
result = solution.addBinary(a, b)
print(result)
