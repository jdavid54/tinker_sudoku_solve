import tkinter as tk
import numpy as np
import time

class SudokuGrid(tk.Frame):
    def __init__(self, root, size, sudoku_list):
        super().__init__(root)
        self.root = root
        self.size = size
        self.sudoku_list = sudoku_list
        self.create_sudoku_grid()
        self.pack()

    def create_sudoku_grid(self):
        self.entries = []
        for i in range(self.size):
            row_entries = []
            for j in range(self.size):
                value = self.sudoku_list[i][j]
                entry = tk.Entry(self, width=2, font=('Arial bold', 18), justify='center')
                if value == 0:
                    entry.config(width=2, font=('Arial', 18))
                entry.grid(row=i, column=j)
                entry.insert(0, str(value))
                row_entries.append(entry)
            self.entries.append(row_entries)

    def update_cell_value(self, row, column, value):
        entry = self.entries[row][column]
        if value != 0:
            entry.config(fg='grey')  # Changement de la couleur du texte en rouge
        else:
            entry.config(fg='red')
        entry.delete(0, tk.END)
        entry.insert(0, str(value))
        self.update()   # Permet d'afficher en temps réel les changements

    def possible(self, y, x, n):
        for i in range(0, self.size):
            if self.sudoku_list[y][i] == n:
                return False
        for i in range(0, self.size):
            if self.sudoku_list[i][x] == n:
                return False
        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range(0, 3):
            for j in range(0, 3):
                if self.sudoku_list[y0+i][x0+j] == n:
                    return False
        return True

    def solve(self):
        end = False
        for y in range(self.size):
            for x in range(self.size):
                #if (y,x) == (8,8) : return True
                if self.sudoku_list[y][x] == 0:
                    for n in range(1, 10):                        
                        if self.possible(y, x, n):
                            #end = True
                            self.sudoku_list[y][x] = n                            
                            self.update_cell_value(y, x, n)  # Mettre à jour la valeur de la cellule
                            end = self.solve()                            
                            if end: return end                            
                            if y == 8:
                                #print(y,x,n)
                                end = True
                                return end                            
                            if not end:
                                self.sudoku_list[y][x] = 0
                                self.update_cell_value(y, x, 0)  # Remettre à zéro la valeur de la cellule                            
                    return end
                else:
                    continue

def main():
    root = tk.Tk()
    root.title("Grille Sudoku")
    label = tk.Label(root, text='Solving ...',font=('Arial', 10))
    label.pack()
    
    sudoku_size = 9
    # Liste de valeurs pour remplir la grille (exemple)
   
    puzzles = [
    [[5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 1, 7, 0]],
    
    [[0, 0, 0, 0, 0, 8, 0, 1, 0],
    [8, 0, 7, 0, 9, 0, 2, 0, 0],
    [0, 2, 0, 0, 0, 7, 6, 0, 4],
    [0, 0, 5, 0, 0, 3, 0, 0, 0],
    [9, 0, 0, 5, 0, 0, 0, 0, 0],
    [0, 4, 0, 0, 6, 0, 3, 0, 8],
    [0, 0, 0, 9, 0, 6, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 0, 0, 2],
    [5, 0, 0, 4, 0, 0, 0, 0, 6]]
    ]
    
    def destroyCallBack():
        root.destroy()
        
    sudoku_list = puzzles[1]
    sudoku_grid = SudokuGrid(root, sudoku_size, sudoku_list)
    B = tk.Button(root, text ="Quit", command = destroyCallBack)
    B.pack()
    start_time = time.time()  # Record start time
    sudoku_grid.solve()
    end_time = time.time()  # Record end time
    t = round(end_time - start_time,2)
    print("All Sudoku puzzles solved in {:.5f} seconds.".format(t))
    print(sudoku_list)
    label.config(text=f'Grid solved in {t} seconds')
    #root.mainloop()

if __name__ == "__main__":
    main()
'''
[[5 3 4 6 7 8 9 1 2]
 [6 7 2 1 9 5 3 4 8]
 [1 9 8 3 4 2 5 6 7]
 [8 5 9 7 6 1 4 2 3]
 [4 2 6 8 5 3 7 9 1]
 [7 1 3 9 2 4 8 5 6]
 [9 6 1 5 3 7 2 8 4]
 [2 8 7 4 1 9 6 3 5]
 [3 4 5 2 8 6 1 7 9]] 

'''