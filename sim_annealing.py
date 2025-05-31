from pyamaze import maze, agent, COLOR, textLabel
from math import exp
import random

def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)

def simulated_annealing(m, schedule, start=None, verbose=False):

    if start is None:
        start = (m.rows, m.cols)  
    goal = m._goal

    current_state = start
    current_value = h(current_state, goal)
    search_path = [current_state] 
    visited = set()  
    visited.add(current_state)

    for t in range(1, 10000):  
        T = schedule(t)  
        if current_value == 0:  
            break
        if T == 0:  
            break

        neighbors = []
        for d in 'ESNW':
            if m.maze_map[current_state][d]: 
                if d == 'E':
                    neighbor = (current_state[0], current_state[1] + 1)
                elif d == 'W':
                    neighbor = (current_state[0], current_state[1] - 1)
                elif d == 'N':
                    neighbor = (current_state[0] - 1, current_state[1])
                elif d == 'S':
                    neighbor = (current_state[0] + 1, current_state[1])

                if neighbor not in visited:
                    neighbors.append(neighbor)

        if not neighbors: 
            break

        next_state = random.choice(neighbors)
        next_value = h(next_state, goal)
        delta = current_value - next_value

        if delta > 0 or random.random() < exp(delta / T):
            current_state = next_state
            current_value = next_value
            search_path.append(current_state)
            visited.add(current_state)

        if verbose:
            print(f"Step: {t}, Current State: {current_state}, Heuristic: {current_value}, Temperature: {T:.2f}")

    fwd_path = {}
    for i in range(len(search_path) - 1):
        fwd_path[search_path[i]] = search_path[i + 1]

    return search_path, fwd_path

def schedule(t):
    return max(0.01, 1 * exp(-0.005 * t))  

if __name__ == "__main__":
    m = maze()
    m.CreateMaze(loadMaze='maze--2024-11-16--14-04-27.csv')

    search_path, fwd_path = simulated_annealing(m, schedule, verbose=True)

    a = agent(m, footprints=True, color=COLOR.blue, filled=True, shape="arrow")
    m.tracePath({a: search_path}, delay=300)

    textLabel(m, 'Simulated Annealing Path Length', len(fwd_path) + 1)
    textLabel(m, 'Simulated Annealing Search Length', len(search_path))

    m.run()
