class Solution:
    def countSeniors(self, details: list[str]) -> int:
        counter = 0
        for passengers in details:
            if int(passengers[11])*10+int(passengers[12]) > 60:
                counter += 1
        return counter


details = ["9751302862F0693","3888560693F7262","5485983835F0649","2580974299F6042","9976672161M6561","0234451011F8013","4294552179O6482"]

solution = Solution()
result = solution.countSeniors(details)
print(result)
