from pyamaze import maze, agent, COLOR
from random import random, randrange

def genetic_algorithm_maze(m, gene_pool, f_thres, ngen=1000, pmut=0.4, start=None):
    if start is None:
        start = (10, 10)  
    goal = m._goal

    pop_size = 500
    state_length = 500  
    population = init_population(pop_size, gene_pool, state_length)

    def fitness_fn(individual):
        current = start
        path_cost = 0
        for move in individual:
            if move not in m.maze_map[current] or not m.maze_map[current][move]:
                break  
            if move == 'E':
                current = (current[0], current[1] + 1)
            elif move == 'W':
                current = (current[0], current[1] - 1)
            elif move == 'N':
                current = (current[0] - 1, current[1])
            elif move == 'S':
                current = (current[0] + 1, current[1])
            path_cost += 1
            if current == goal:
                return f_thres + 100 
       
        distance_to_goal = abs(goal[0] - current[0]) + abs(goal[1] - current[1])
        return -distance_to_goal + path_cost

    for gen in range(ngen):
        population = [
            mutate(recombine(*select(2, population, fitness_fn)), gene_pool, pmut)
            for _ in range(len(population))
        ]

        fittest_individual = max(population, key=fitness_fn)

        if fitness_fn(fittest_individual) == f_thres:
            print(f"Solution found in generation {gen + 1}")
            return extract_path(start, fittest_individual, m)

    return extract_path(start, max(population, key=fitness_fn), m)


def recombine(x, y):
    n = len(x)
    c = randrange(0, n)
    return x[:c] + y[c:]


def mutate(x, gene_pool, pmut):
    if random() < pmut:
        n = len(x)
        c = randrange(0, n)
        new_gene = gene_pool[randrange(0, len(gene_pool))]
        return x[:c] + [new_gene] + x[c + 1:]
    return x


def select(k, population, fitness_fn):
    weights = [max(0, fitness_fn(ind)) for ind in population]
    return [population[randrange(0, len(population))] for _ in range(k)]


def init_population(pop_size, gene_pool, state_length):
    return [
        [gene_pool[randrange(0, len(gene_pool))] for _ in range(state_length)]
        for _ in range(pop_size)
    ]


def extract_path(start, individual, m):
    current = start
    path = [current]
    for move in individual:
        if move not in m.maze_map[current] or not m.maze_map[current][move]:
            break  
        if move == 'E':
            current = (current[0], current[1] + 1)
        elif move == 'W':
            current = (current[0], current[1] - 1)
        elif move == 'N':
            current = (current[0] - 1, current[1])
        elif move == 'S':
            current = (current[0] + 1, current[1])
        path.append(current)
        if current == m._goal:
            break  
    return path


if __name__ == '__main__':
    m = maze()
    m.CreateMaze(1, 1, loadMaze='maze--2024-11-16--14-04-27.csv')

    gene_pool = ['N', 'E', 'S', 'W']  

    path = genetic_algorithm_maze(m, gene_pool, f_thres=0, ngen=500, pmut=0.2)

    a = agent(m, footprints=True, color=COLOR.red)
    m.tracePath({a: path}, showMarked=True)
    m.run()
