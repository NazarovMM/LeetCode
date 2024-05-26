class Solution:
    def myPrint(output: str) -> int:
        if (output == '-' or output == '+' or output == '.') and len(output) == 1:
            return 0
        if not output:
            return 0
        if (-2)**31 > int(output):
            return (-2)**31
        elif int(output) > 2**31-1:
            return 2**31-1
        else:
            return int(output)

    def myAtoi(self, s: str) -> int:
        ch_list = list(x for x in s)
        output = ''
        flag = False
        for i in range(len(ch_list)):
            if (ch_list[i].isalpha() or ch_list[i] == '.') and flag == False:
                return 0
            elif ch_list[i] == ' ' and flag == False:
                next
            elif (ch_list[i] == '-' or ch_list[i] == '+') and flag == False:
                output += ch_list[i]
                flag = True
            elif not ch_list[i].isdigit() and flag:
                return Solution.myPrint(output)
            elif ch_list[i].isdigit():
                output += ch_list[i]
                flag = True
        return Solution.myPrint(output)


s = " "
solution = Solution()
result = solution.myAtoi(s)
print(result)
