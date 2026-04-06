class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == '.':
                    continue
                
                val = int(board[r][c]) - 1
                mask = 1 << val

                if mask & rows[r] or mask & cols[c] or mask & boxes[r//3*3 + c//3]:
                    return False
                
                rows[r] |= mask
                cols[c] |= mask
                boxes[r//3*3 + c//3] |= mask

        return True             