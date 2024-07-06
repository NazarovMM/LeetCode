class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = 0
        pers = 1
        while time > 0:
            if pers < n and direction == 0:
                pers += 1
            elif pers == n and direction == 0:
                pers -= 1
                direction = 1
            elif pers > 1 and direction == 1:
                pers -= 1
            elif pers == 1 and direction == 1:
                pers += 1
                direction = 0
            time -= 1
        return pers


n = 18
time = 38
solution = Solution()
result = solution.passThePillow(n, time)
print(result)
