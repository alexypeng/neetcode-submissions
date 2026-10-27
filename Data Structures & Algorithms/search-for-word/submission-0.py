class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        found = False

        def backtrack(r, c, seen, cur):
            if cur != word[:len(cur)]:
                return
            if len(cur) == len(word):
                if cur == word:
                    nonlocal found
                    found = True
                return

            if r > 0 and (r-1, c) not in seen:
                seen.add((r-1, c))
                backtrack(r-1, c, seen, cur + board[r-1][c])
                seen.remove((r-1, c))
            if c > 0 and (r, c-1) not in seen:
                seen.add((r, c-1))
                backtrack(r, c-1, seen, cur + board[r][c-1])
                seen.remove((r, c-1))
            if r < len(board) - 1 and (r+1, c) not in seen:
                seen.add((r+1, c))
                backtrack(r+1, c, seen, cur + board[r+1][c])
                seen.remove((r+1, c))
            if c < len(board[0]) - 1 and (r, c+1) not in seen:
                seen.add((r, c+1))
                backtrack(r, c+1, seen, cur + board[r][c+1])
                seen.remove((r, c+1))
            
        for r in range(len(board)):
            for c in range(len(board[0])):
                backtrack(r, c, set({(r, c)}), board[r][c])
        
        return found

