#BRUTE FORCE
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in range(9):
            seen=set()
            for i in range(9):
                if board[row][i]==".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for col in range(9):
            seen=set()
            for i in range(9):
                if board[i][col]==".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])

        for square in range(9):
            seen=set()
            for i in range(3):
                for j in range(3):
                    row=(square//3)*3+i
                    col=(square % 3)*3+j
                    if board[row][col]==".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True

#HASH MAP
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        cols= defaultdict(set)
        rows= defaultdict(set)
        squares= defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r//3,c//3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])

        return True

#BITMASK
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows=[0]*9
        cols=[0]*9
        squares=[0]*9

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue

                val=int(board[r][c])-1
                if (1<<val) & rows[r]:
                    return False
                if (1<<val) & cols[c]:
                    return False
                if (1<<val) & squares[(r//3)*3+(c//3)]:
                    return False

                rows[r]|=(1<<val)
                cols[c]|=(1<<val)
                squares[(r//3)*3+(c//3)]|=(1<<val)

        return True