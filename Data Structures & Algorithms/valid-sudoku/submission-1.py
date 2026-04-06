class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue

                num = int(board[r][c]) - 1
                mask = (1 << num)

                if rows[r] & mask:
                    return False
                if cols[c] & mask:
                    return False
                if boxes[((r//3) * 3) + c//3] & mask:
                    return False
                
                rows[r] |= mask
                cols[c] |= mask
                boxes[((r//3) * 3) + c//3] |= mask
        return True