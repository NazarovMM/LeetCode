class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        numbers = {'2': ['a', 'b', 'c'],
                   '3': ['d', 'e', 'f'],
                   '4': ['g', 'h', 'i'],
                   '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'],
                   '9': ['w', 'x', 'y', 'z']}
        if digits == "":
            return []
        result = ['']
        for digit in digits:
            temp = []
            for combination in result:
                for letter in numbers[digit]:
                    temp.append(combination + letter)
            result = temp
        return result


digits = "234"

solution = Solution()
result = solution.letterCombinations(digits)
print(result)
