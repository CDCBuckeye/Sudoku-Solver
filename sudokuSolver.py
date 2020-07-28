class Sudoku:
    def __init__(self, board):
        self.board = board
        self.blockSize = 3

    def getEmpty(self):
        '''
        Return a coordinate of an empty spot.
        Return None if there is not any.
        '''
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == 0:
                    return (row, col)
        return None

    def isValid(self, row, col, num):
        '''
        Check if it is OK to put num at (row, col).
        '''
        for i in range(len(self.board)):
            # check cols
            if self.board[i][col] == num: return False
            # check rows
            if self.board[row][i] == num: return False
        # check sub blocks
        for r in range(row - row % self.blockSize, row - row % self.blockSize + self.blockSize):
            for c in range(col - col % self.blockSize, col - col % self.blockSize + self.blockSize):
                if self.board[r][c] == num: return False
        return True


    def backtracking(self):
        '''
        Solve the sudoku problem using backtracking.
        '''
        # no empty spot -> solved
        empty = self.getEmpty()
        if not empty: return True
        else:
            row, col = empty
        for i in range(1, len(self.board) + 1):
            if self.isValid(row, col, i):
                self.board[row][col] = i
                if self.backtracking(): return True
                self.board[row][col] = 0
        return False
    
    def __str__(self):
        lines = []
        for row in range(len(self.board)):
            rowLine = ''
            for col in range(len(self.board)):
                num = ' ' + self.board[row][col].__str__() + ' '
                if (col + 1) % self.blockSize == 0: 
                    rowLine += num + '|'
                elif col == 0: 
                    rowLine = '|' + num
                else: 
                    rowLine += num
            lines.append(rowLine)
            if (row + 1) % self.blockSize == 0: lines.append('-' * len(rowLine))
        lines.insert(0, '-' * len(rowLine))
        return '\n'.join(lines)

if __name__ == '__main__':
    board = [
        [0,0,8,4,0,0,0,9,0],
        [0,9,0,6,0,3,7,0,1],
        [0,0,3,2,0,0,5,0,8],
        [0,0,0,8,4,0,6,3,0],
        [0,8,5,0,0,2,0,1,0],
        [9,3,0,0,5,0,0,0,7],
        [0,2,0,0,0,8,0,5,4],
        [0,0,0,3,0,7,0,0,0],
        [0,0,0,0,0,0,3,0,0]
    ]
    # board = [
    #     [0,0,0,0,6,0,0,0,0],
    #     [0,4,0,5,8,0,0,6,0],
    #     [0,7,0,0,0,2,8,0,0],
    #     [0,0,0,8,0,0,4,0,5],
    #     [8,0,0,0,0,0,2,0,0],
    #     [0,0,0,0,0,6,0,0,0],
    #     [0,2,7,0,0,0,0,3,0],
    #     [4,0,0,7,3,0,0,0,2],
    #     [5,0,9,0,0,4,0,7,0]
    # ]
    sudoku = Sudoku(board)
    print('Intial board: ')
    print(sudoku)
    if sudoku.backtracking():
        print('Solution found: ')
        print(sudoku)
    else:
        print('No solution found.')
