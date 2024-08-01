class Solution:
    def interpret(self, command: str) -> str:
        output = ''
        while command:
            if command.find('G') == 0:
                command = command.removeprefix('G')
                output += 'G'
            elif command.find('(al)') == 0:
                command = command.removeprefix('(al)')
                output += 'al'
            else:
                command = command.removeprefix('()')
                output += 'o'
        return output


command = "G()(al)"

solution = Solution()
result = solution.interpret(command)
print(result)
