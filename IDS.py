from pyamaze import maze, agent, COLOR, textLabel

def DLS(m, current, limit, explored, dlsPath):
    if current == m._goal: 
        return True

    if limit <= 0:
        return False

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

            if child not in explored:
                explored.append(child)
                dlsPath[child] = current
                if DLS(m, child, limit - 1, explored, dlsPath):
                    return True

    return False

def IDS(m, start=None, max_depth = 5):
    if start is None:
        start = (m.rows, m.cols)

    print(f"Starting IDS from: {start}, Goal: {m._goal}")

    for depth in range(1, max_depth + 1):  
        print(f"Exploring with depth limit: {depth}")
        explored = [start]
        dlsPath = {}
        if DLS(m, start, depth, explored, dlsPath):
            fwdPath = {}
            cell = m._goal
            while cell != start:
                fwdPath[dlsPath[cell]] = cell
                cell = dlsPath[cell]
            print(f"Solution found at depth: {depth}")
            return explored, dlsPath, fwdPath

    print("No solution found within the depth limit.")
    return None, None, None

if __name__ == '__main__':
    m = maze() 
    m.CreateMaze(loadMaze='maze--2024-11-16--14-04-27.csv')

    start = (m.rows, m.cols)
    goal = (1, 1)
    m._goal = goal

    dSearch, idsPath, fwdPath = IDS(m, start=start, max_depth = 30)

    if fwdPath:
        a = agent(m, *start, goal=goal, footprints=True, shape='arrow', color=COLOR.green)
        m.tracePath({a: fwdPath}, showMarked=True)

        #b = agent(m, *start, goal=goal, footprints=True, color=COLOR.blue, filled=True)
        #m.tracePath({b: dSearch}, showMarked=True)

        m.run()
    else:
        print("No solution found within the given depth limit.")
