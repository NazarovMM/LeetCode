class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maximum = 0
        for obj in accounts:
            buff = 0
            buff += sum([ch for ch in obj])
            if buff > maximum:
                maximum = buff
        return maximum


accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
solution = Solution()
result = solution.maximumWealth(accounts)
print(result)
