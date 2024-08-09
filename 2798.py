class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        counter = 0
        for hour in hours:
            if hour >= target:
                counter += 1
        return counter


hours = [5, 1, 4, 2, 2]
target = 6

solution = Solution()
result = solution.numberOfEmployeesWhoMetTarget(hours, target)
print(result)
