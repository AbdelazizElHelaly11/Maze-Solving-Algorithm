# Maze Solving Algorithms Project

This project implements various search algorithms and machine learning approaches to solve maze navigation problems. The project includes both traditional search algorithms and modern machine learning techniques.

## Project Structure

The project contains the following main components:

### Search Algorithms
- `Astar.py` - A* search algorithm implementation
- `BFS.py` - Breadth-First Search implementation
- `DFS.py` - Depth-First Search implementation
- `IDS.py` - Iterative Deepening Search implementation
- `UCS.PY` - Uniform Cost Search implementation
- `Greedy-search.py` - Greedy Best-First Search implementation
- `Hill_Climbing.py` - Hill Climbing algorithm implementation
- `sim_annealing.py` - Simulated Annealing implementation

### Machine Learning Approaches
- `Qlearning.py` - Q-Learning implementation for maze navigation
- `genetic_algo.py` - Genetic Algorithm implementation

### Support Files
- `maze.py` - Core maze generation and visualization
- `visuals.py` - Visualization utilities
- `performance.py` - Performance measurement tools
- `pyMaze.py` - Maze environment implementation

## Features

1. **Multiple Search Algorithms**
   - Traditional graph search algorithms (BFS, DFS, A*, etc.)
   - Local search algorithms (Hill Climbing, Simulated Annealing)
   - Each algorithm is optimized for maze navigation

2. **Machine Learning Solutions**
   - Q-Learning with customizable parameters
   - Genetic Algorithm with configurable population size and mutation rate
   - Performance tracking and visualization

3. **Visualization Tools**
   - Real-time maze solving visualization
   - Path tracking and performance metrics
   - Customizable maze generation

## Requirements

- Python 3.x
- Required packages:
  - numpy
  - random
  - json
  - time
  - pyamaze

## Usage

### Running Search Algorithms

```python
from pyamaze import maze, agent
from BFS import bfs  # or any other algorithm

# Create a maze
m = maze()
m.CreateMaze()

# Run the algorithm
path = bfs(m)

# Visualize the solution
a = agent(m, footprints=True)
m.tracePath({a: path})
m.run()
```

### Running Q-Learning

```python
from Qlearning import QLearningMaze

# Create maze and initialize Q-Learning
m = maze(20, 20)
m.CreateMaze()
q_learning_agent = QLearningMaze(m, ['N', 'E', 'W', 'S'])

# Train the agent
q_learning_agent.train(episodes=1000)

# Get and visualize the solution
policy = q_learning_agent.get_policy()
path = q_learning_agent.generate_path((1, 1), m._goal, policy)
```

### Running Genetic Algorithm

```python
from genetic_algo import genetic_algorithm_maze

# Create maze and run genetic algorithm
m = maze()
m.CreateMaze()
gene_pool = ['N', 'E', 'S', 'W']
path = genetic_algorithm_maze(m, gene_pool, f_thres=0, ngen=500, pmut=0.2)
```

## Performance Metrics

The project includes tools to measure and compare the performance of different algorithms:
- Success rate tracking
- Steps per episode
- Training time measurement
- Path length comparison

## Contributing

Feel free to contribute to this project by:
1. Adding new algorithms
2. Improving existing implementations
3. Adding new features or visualizations
4. Reporting bugs or suggesting improvements

## License

This project is open source and available under the MIT License. 