class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        output = 0
        for i in range(len(seats)):
            if seats[i] != students[i]:
                output += abs(seats[i]-students[i])
        return output


seats = [2, 2, 6, 6]
students = [1, 3, 2, 6]
solution = Solution()
result = solution.minMovesToSeat(seats, students)
print(result)
