class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        
        output = []
        buff = {}
        # разбиение на подгруппы с одинаковым содержанием элементов
        for i in range(len(groupSizes)):
            if groupSizes[i] not in buff.keys():
                buff[groupSizes[i]] = [i]
            else:
                buff[groupSizes[i]].append(i)
        # разбиение на итоговые подгруппы с учитыванием кол-ва элементов в подгруппе
        for key in buff.keys():
            values = buff.get(key)
            if len(values) > 1:
                chunk_size = key
                chunks = list(
                    values[i: i + chunk_size]
                    for i in range(0, len(values), chunk_size)
                )
                for chunk in chunks:
                    output.append(chunk)
            else:
                output.append(values)

        return output


groupSizes = [3, 3, 3, 3, 3, 1, 3]

solution = Solution()
result = solution.groupThePeople(groupSizes)
print(result)
