# 🏆 Maze Solver

## 📌 Description
This Python project generates and solves a maze using recursion and depth-first search (DFS). The maze is displayed in a graphical window using Tkinter and can be visually solved by the program.

## 🚀 Features
- **Maze Generation**: Creates a random maze of any size.
- **Recursive Backtracking**: Uses depth-first search (DFS) to generate and solve the maze.
- **Graphical Visualization**: Displays the maze using Tkinter with a simple GUI.
- **Customizable Parameters**: Allows users to define the number of rows, columns, and cell sizes.
- **Automated Unit Tests**: Includes test cases to verify maze generation and solving.

---

## 📂 Project Structure
```
📦 maze-solver
│-- 📄 main.py          # Entry point of the application
│-- 📄 window.py        # Handles the Tkinter GUI window
│-- 📄 drawing.py       # Defines lines, points, and cell drawing functions
│-- 📄 maze.py          # Implements maze generation and solving
│-- 📄 tests.py         # Unit tests for maze generation and solving
│-- 📄 README.md        # Project documentation
```

## ⚡ Installation & Usage

1️⃣ Clone the Repository
```
git clone https://github.com/YOUR-USERNAME/maze-solver.git
cd maze-solver
```
2️⃣ Install Dependencies
Ensure you have Python installed (>=3.6). This project only uses Tkinter, which is built into Python.

3️⃣ Run the Program
```
python main.py
```

This will generate and solve a maze in a pop-up window.

## 🛠️ Customization
Modify the following parameters in main.py:
```
win = Window(1000, 1000)  # Window size
m = Maze(10, 10, 10, 10, 40, 40, win, 10)  # Maze properties
```
- Maze size: Adjust num_rows and num_cols
- Cell size: Modify cell_size_x and cell_size_y
- Seed value: Set a fixed seed for repeatable mazes

## 🧪 Running Tests
To run the unit tests:
```
python -m unittest tests.py
```

## 🎯 To-Do & Future Improvements
- [] Add a GUI button to regenerate the maze dynamically.
- [] Implement different maze-solving algorithms (e.g., BFS, A*).
- [] Allow user interaction to solve the maze manually.

## 🤝 Contributing
Feel free to fork the repository, create feature branches, and submit pull requests.

## 📜 License
This project is licensed under the MIT License.
