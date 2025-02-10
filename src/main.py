from window import Window
from drawing import Line, Point, Cell
from maze import Maze

def main():
    win = Window(1000, 1000)
    m = Maze(10, 10, 10, 10, 40, 40, win, 10)
    m._create_cells()
    m.solve()
    win.wait_for_close()
    
main()
    