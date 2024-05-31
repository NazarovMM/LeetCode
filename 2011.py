class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        dictionary = {"X++": 1, "++X": 1, "--X": -1, "X--": -1}
        output = 0
        for x in operations:
            if x in dictionary.keys():
                output += dictionary.get(x)
        return output


operations = ["X++","++X","--X","X--"]
solution = Solution()
result = solution.finalValueAfterOperations(operations)
print(result)
