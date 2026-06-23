class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for idx_row, row in enumerate(board):
            for idx_col, el in enumerate(row):
                if el == ".":
                    continue
                idx_box =(idx_row // 3, idx_col //3)
                if (
                    el in cols[idx_col]
                    or el in rows[idx_row]
                    or el in boxes[idx_box]
                ):
                    return False
                cols[idx_col].add(el)
                rows[idx_row].add(el)
                boxes[idx_box].add(el)
        return True