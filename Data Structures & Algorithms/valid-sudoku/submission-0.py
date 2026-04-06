class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                box_no = (r//3, c//3)
                num = board[r][c]
                if num == ".":
                    continue
                else:
                    if num in rows[r] or num in cols[c] or num in boxes[box_no]:
                        return False
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_no].add(num)
        return True