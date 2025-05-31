from pyamaze import maze, agent, COLOR, textLabel
from queue import PriorityQueue
from math import sqrt
def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)

def h1(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def greedy_best_first_search(m, start=None):
    if start is None:
        start = (m.rows, m.cols) 
    goal = m._goal

    open = PriorityQueue()
    open.put((h(start, goal), start))  
    search_path = []  
    gbfs_path = {}  

    while not open.empty():
        current = open.get()[1]
        search_path.append(current)

        if current == goal:
            break

        for d in 'ESNW':
            if m.maze_map[current][d]:
                if d == 'E':
                    child = (current[0], current[1] + 1)
                elif d == 'W':
                    child = (current[0], current[1] - 1)
                elif d == 'N':
                    child = (current[0] - 1, current[1])
                elif d == 'S':
                    child = (current[0] + 1, current[1])

                if child not in gbfs_path:  
                    gbfs_path[child] = current
                    open.put((h(child, goal), child))

    fwd_path = {}
    cell = goal
    while cell != start:
        fwd_path[gbfs_path[cell]] = cell
        cell = gbfs_path[cell]

    return search_path, gbfs_path, fwd_path

if __name__ == '__main__':
    m = maze(6, 6)
    m.CreateMaze(loadMaze='maze--2024-11-16--14-04-27.csv')

    search_path, gbfs_path, fwd_path = greedy_best_first_search(m)

    a = agent(m, footprints=True, color=COLOR.blue, filled=True)  
    b = agent(m, footprints=True, color=COLOR.yellow, filled=True, goal=(m.rows, m.cols))  
    c = agent(m, footprints=True, color=COLOR.red)  

    m.tracePath({a: search_path}, delay=300)
    m.tracePath({b: gbfs_path}, delay=300)
    m.tracePath({c: fwd_path}, delay=300)

    textLabel(m, 'GBFS Path Length', len(fwd_path) + 1)
    textLabel(m, 'GBFS Search Length', len(search_path))

    m.run()
