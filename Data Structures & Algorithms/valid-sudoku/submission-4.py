class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board[0]))]
        boxes = [set() for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue
                
                box = 3 * (i // 3) + j // 3
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in boxes[box]:
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                boxes[box].add(board[i][j])
        
        return True