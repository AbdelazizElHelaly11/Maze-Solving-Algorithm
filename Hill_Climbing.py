from pyamaze import maze, agent, COLOR, textLabel
from math import sqrt

def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)  

def hill_climbing_with_slope(m, start=None):
    if start is None:
        start = (m.rows, m.cols)

    current = start
    goal = m._goal
    search_path = [current]
    visited = set()

    while current != goal:
        neighbors = []
        slopes = []

        for d in 'ESNW':
            if m.maze_map[current][d]:  
                if d == 'E':
                    neighbor = (current[0], current[1] + 1)
                elif d == 'W':
                    neighbor = (current[0], current[1] - 1)
                elif d == 'N':
                    neighbor = (current[0] - 1, current[1])
                elif d == 'S':
                    neighbor = (current[0] + 1, current[1])

                if neighbor not in visited:
                    neighbors.append(neighbor)
                    slope = h(current, goal) - h(neighbor, goal) 
                    slopes.append(slope)

        if not neighbors:  
            break

      
        max_slope_idx = slopes.index(max(slopes))
        best_neighbor = neighbors[max_slope_idx]

        if slopes[max_slope_idx] <= 0: 
            break

        visited.add(current)
        current = best_neighbor
        search_path.append(current)

    fwd_path = {}
    for i in range(len(search_path) - 1):
        fwd_path[search_path[i]] = search_path[i + 1]

    return search_path, fwd_path

if __name__ == '__main__':
    m = maze()
    m.CreateMaze(loadMaze='maze--2024-11-16--14-04-27.csv')

    search_path, fwd_path = hill_climbing_with_slope(m)

    a = agent(m, footprints=True, color=COLOR.blue, filled=True, shape='arrow', goal=m._goal)

    m.tracePath({a: search_path}, delay=300)

    # Display information
    textLabel(m, 'Hill Climbing Path Length', len(fwd_path) + 1)
    textLabel(m, 'Hill Climbing Search Length', len(search_path))

    m.run()
