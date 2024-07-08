class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(x for x in range(1, n+1))
        current = 0
        while len(friends) != 1:
            next_del = (current + k - 1) % len(friends)
            friends.pop(next_del)
            current = next_del
        return friends[0]


n = 5
k = 2

solution = Solution()
result = solution.findTheWinner(n, k)
print(result)