import tkinter as tk

class SudokuGUI:
    def __init__(self, root, board):
        self.root = root
        self.board = board
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.makeboard()

    def makeboard(self):
        for row in range(3):
            for col in range(3):
                frame = tk.Frame(self.root, borderwidth=2, relief="solid")
                frame.grid(row=row, column=col, padx=1, pady=1)
                for i in range(3):
                    for j in range(3):
                        r = row * 3 + i
                        c = col * 3 + j
                        entry = tk.Entry(frame, width=5, justify='center')
                        if self.board[r][c] != 0:
                            entry.insert(0, self.board[r][c])
                            entry.config(state='readonly')  
                        entry.grid(row=i, column=j, padx=1, pady=1)
                        self.entries[r][c] = entry

    def set_value(self, r, c, value):
        entry = self.entries[r][c]
        if value != 0:
            entry.config(state='normal')
            entry.delete(0, tk.END)
            entry.insert(0, value)
            entry.config(state='readonly')
        else:
            entry.config(state='normal')
            entry.delete(0, tk.END)
        self.root.update_idletasks()  

def isValid(board, r, c, k):
    valid_in_row = k not in board[r]
    valid_in_column = k not in [board[i][c] for i in range(9)]
    valid_in_box = k not in [board[i][j] for i in range(r // 3 * 3, r // 3 * 3 + 3) for j in range(c // 3 * 3, c // 3 * 3 + 3)]
    return valid_in_row and valid_in_column and valid_in_box

def solveSudoku(board, gui, r=0, c=0):
    if r == 9:
        return True
    elif c == 9:
        return solveSudoku(board, gui, r + 1, 0)
    elif board[r][c] != 0:
        return solveSudoku(board, gui, r, c + 1)
    else:
        for number in range(1, 10):
            if isValid(board, r, c, number):
                board[r][c] = number
                gui.set_value(r, c, number)  
                gui.root.update()  
                if solveSudoku(board, gui, r, c + 1):
                    return True
                board[r][c] = 0
                gui.set_value(r, c, 0) 
                gui.root.update() 
        return False

def main():
    board = [[0, 0, 4, 0, 5, 0, 0, 0, 0],
             [9, 0, 0, 7, 3, 4, 6, 0, 0],
             [0, 0, 3, 0, 2, 1, 0, 4, 9],
             [0, 3, 5, 0, 9, 0, 4, 8, 0],
             [0, 9, 0, 0, 0, 0, 0, 3, 0],
             [0, 7, 6, 0, 1, 0, 9, 2, 0],
             [3, 1, 0, 9, 7, 0, 2, 0, 0],
             [0, 0, 9, 1, 8, 2, 0, 0, 3],
             [0, 0, 0, 0, 6, 0, 1, 0, 0]]

    root = tk.Tk()
    root.title("Sudoku Solver")
    gui = SudokuGUI(root, board)

    solve_button = tk.Button(root, text="Solve", command=lambda: solveSudoku(board, gui))
    solve_button.grid(row=3, column=1, columnspan=3)

    root.mainloop()

if __name__ == "__main__":
    main()
