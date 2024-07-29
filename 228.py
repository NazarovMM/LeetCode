class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums: #проверка на пустой список на входе
            return []
        output = [] #список для вывода
        point = 0 #переменная содержащее последнее значение, которое подходит для группы 
        start = nums[0] # начальный элемент
        buff = 1 # переменная хранящая разницу между началом и концом группы
        for i in range(1, len(nums)):
            end = nums[i]
            if start+buff == end:
                buff += 1
                point = end
            elif buff == 1:
                output.append("{}".format(start))
                start = nums[i]
                buff = 1
            else:
                output.append("{}->{}".format(start, point))
                start = nums[i]
                buff = 1
        if buff == 1:
            output.append("{}".format(start))
        else:
            output.append("{}->{}".format(start, point))
        return output


nums = []

solution = Solution()
result = solution.summaryRanges(nums)
print(result)
