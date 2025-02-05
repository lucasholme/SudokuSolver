# 🧩 Sudoku Solver GUI

This is a **Sudoku Solver** built using **Tkinter** for the graphical user interface. It allows users to visualize the process of solving a **9x9 Sudoku puzzle** using a **backtracking algorithm**.

## 🚀 Features

- ✅ **Graphical Interface** -- Uses `Tkinter` to display the Sudoku board in a user-friendly manner.
- ✅ **Pre-Filled Board** -- Displays given Sudoku clues as read-only cells.
- ✅ **Interactive Solving** -- Solves the Sudoku step-by-step with real-time updates.
- ✅ **Backtracking Algorithm** -- Implements a recursive solution to find the correct board configuration.
- ✅ **Auto-Update UI** -- Dynamically updates the board during the solving process.

## 📥 Installation

Ensure you have **Python 3.x** installed on your system.

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/your-username/sudoku-solver.git
```

### 2️⃣ Install Dependencies

The only required dependency is `tkinter`, which comes pre-installed with Python.

🛠️ Usage
---------

### 1️⃣ Run the Sudoku Solver

```
python sudoku_solver.py
```
### 2️⃣ How It Works

-   The script **displays the Sudoku board** with some **pre-filled numbers**.
-   Click the **"Solve" button** to watch the puzzle **solve itself in real-time**.
-   Uses a **backtracking algorithm** to find the correct solution efficiently.

🔢 Sudoku Board Structure
-------------------------

The Sudoku board is stored as a **9x9 2D list**, where:

-   `0` represents an **empty cell**.
-   Non-zero values represent **pre-filled numbers** that cannot be changed.

Example starting board:

```board = [
    [0, 0, 4, 0, 5, 0, 0, 0, 0],
    [9, 0, 0, 7, 3, 4, 6, 0, 0],
    [0, 0, 3, 0, 2, 1, 0, 4, 9],
    [0, 3, 5, 0, 9, 0, 4, 8, 0],
    [0, 9, 0, 0, 0, 0, 0, 3, 0],
    [0, 7, 6, 0, 1, 0, 9, 2, 0],
    [3, 1, 0, 9, 7, 0, 2, 0, 0],
    [0, 0, 9, 1, 8, 2, 0, 0, 3],
    [0, 0, 0, 0, 6, 0, 1, 0, 0]]
```

🔥 Example Output
-----------------

The solver will fill in the board dynamically. Example of solved output:

```[[8, 6, 4, 2, 5, 9, 3, 1, 7],
 [9, 2, 1, 7, 3, 4, 6, 5, 8],
 [5, 7, 3, 6, 2, 1, 8, 4, 9],
 [1, 3, 5, 8, 9, 6, 4, 7, 2],
 [6, 9, 2, 4, 7, 5, 1, 3, 8],
 [4, 7, 6, 3, 1, 2, 9, 8, 5],
 [3, 1, 8, 9, 7, 5, 2, 6, 4],
 [7, 5, 9, 1, 8, 2, 4, 9, 3],
 [2, 4, 7, 5, 6, 3, 1, 9, 8]]
```

🛑 Notes
--------

-   ⚠️ **Real-Time Updates** -- The board updates dynamically as the algorithm runs.
-   ⚠️ **Backtracking Efficiency** -- The algorithm efficiently finds a solution but may take longer for complex boards.

📜 License
----------

This project is open-source under the MIT License.
