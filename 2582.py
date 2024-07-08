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


class Solution2:
    def passThePillow(self, n: int, time: int) -> int:
        direction = 1
        pers = 1
        while time > 0:
            pers += direction
            if pers == n or pers == 1:
                direction = direction*(-1)
            time -= 1
        return pers


# переписать эффективнее
n = 18
time = 38
solution = Solution2()
result = solution.passThePillow(n, time)
print(result)
