import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        
    def test_maze_create_only_1_col(self):
        num_cols = 1
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        
    def test_maze_create_only_1_row(self):
        num_cols = 10
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        
    def test_maze_create_large_cells(self):
        large_size_x = 50
        large_size_y = 60
        m1 = Maze(0, 0, 10, 10, large_size_x, large_size_y)
        self.assertEqual(m1._cell_size_x, large_size_x)
        self.assertEqual(m1._cell_size_y, large_size_y)

    def test_maze_break_entrance_and_exit(self):
        rows = 10
        cols = 10
        m1 = Maze(0, 0, rows, cols, 30, 30)
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[rows - 1][cols - 1].has_bottom_wall, False)
        
    def test_reset_cells_visited(self):
        rows = 10
        cols = 10
        m1 = Maze(0, 0, rows, cols, 30, 30)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(cell.visited, False)
       
if __name__ == "__main__":
    unittest.main()