class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        status = True

        # Начало проверки строки
        for row in range(0, 9, 1):
            ch_list = []
            for ch in board[row]:
                if ch == '.':
                    pass
                else:
                    if ch in ch_list:
                        status = False
                        break
                    else:
                        ch_list.append(ch)
        # Конец проверки строки

        # Начало проверки столбца
        for column in range(0, 9, 1):
            ch_list = []
            for ch in range(0, 9, 1):
                if board[ch][column] == '.':
                    pass
                else:
                    if board[ch][column] in ch_list:
                        status = False
                        break
                    else:
                        ch_list.append(board[ch][column])
        # Конец проверки столбца

        # Начало проверки квадарата
        for row_cube in range(0, 9, 3):
            for column_cube in range(0, 9, 3):
                ch_list = []
                for i in range(0, 3, 1):
                    for j in range(0, 3, 1):
                        if board[row_cube+i][column_cube+j] == '.':
                            pass
                        else:
                            if board[row_cube+i][column_cube+j] in ch_list:
                                status = False
                                break
                            else:
                                ch_list.append(
                                    board[row_cube+i][column_cube+j])
        # Конец проверки квадарата
        return status


board =[[".",".","4",".",".",".","6","3","."],
        [".",".",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".","9","."],
        [".",".",".","5","6",".",".",".","."],
        ["4",".","3",".",".",".",".",".","1"],
        [".",".",".","7",".",".",".",".","."],
        [".",".",".","5",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]]
solution = Solution()
result = solution.isValidSudoku(board)
print(result)
