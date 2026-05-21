class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row check
        for i in range(9):
            row_check = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row_check:
                    return False
                row_check.add(board[i][j])
        # column check
        for i in range(9):
            col_check = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in col_check:
                    return False
                col_check.add(board[j][i])
        # box check
        seen = [[set(),set(),set()],[set(),set(),set()],[set(),set(),set()]]
        for i in range(9):
            for j in range(9):
                box_row = i // 3
                box_col = j // 3
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen[box_row][box_col]:
                    return False
                seen[box_row][box_col].add(board[i][j])

        return True
       