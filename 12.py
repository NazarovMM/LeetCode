class Solution:
    def intToRoman(self, num: int) -> str:
        output = ""
        thousands = num//1000
        hundreds = num % 1000//100
        tens = num % 100//10
        ones = num % 10
        if thousands != 0:
            for i in range(1, thousands+1):
                output += "M"
        if hundreds != 0:
            if hundreds <= 3:
                for j in range(1, hundreds+1):
                    output += "C"
            elif hundreds == 4:
                output += "CD"
            elif hundreds == 5:
                output += "D"
            elif 5 < hundreds < 9:
                output += "D"
                for k in range(1, hundreds-4):
                    output += "C"
            else:
                output += "CM"
        if tens != 0:
            if tens <= 3:
                for l in range(1, tens+1):
                    output += "X"
            elif tens == 4:
                output += "XL"
            elif tens == 5:
                output += "L"
            elif 5 < tens < 9:
                output += "L"
                for m in range(1, tens-5+1):
                    output += "X"
            else:
                output += "XC"
        if ones != 0:
            if ones <= 3:
                for n in range(1, ones+1):
                    output += "I"
            elif ones == 4:
                output += "IV"
            elif ones == 5:
                output += "V"
            elif 5 < ones < 9:
                output += "V"
                for o in range(1, ones-5+1):
                    output += "I"
            else:
                output += "IX"
        return output


num = 1994
solution = Solution()
result = solution.intToRoman(num)
print(result)