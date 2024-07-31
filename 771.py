class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        for ch in jewels:
            counter += stones.count(ch)
        return counter


jewels = "aA"
stones = "aAAbbbb"

solution = Solution()
result = solution.numJewelsInStones(jewels, stones)
print(result)
