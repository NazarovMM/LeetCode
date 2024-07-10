class Solution:
    def minOperations(self, logs: list[str]) -> int:
        counter = 0
        for ch in logs:
            if ch not in "../":
                counter += 1
            elif ch == "../" and counter != 0:
                counter -= 1
            else:
                continue
        return counter


logs = ["d1/", "d2/", "../", "d21/", "./"]

solution = Solution()
result = solution.minOperations(logs)
print(result)
