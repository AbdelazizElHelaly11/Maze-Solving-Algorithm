# 🧠 Maze Solving Algorithms Project

This project implements and compares a wide range of algorithms to solve maze navigation problems, using both **traditional search methods** and **modern machine learning approaches**. The maze environment is built with `pyamaze`, and performance is evaluated on a 100×100 grid.

---

## 📁 Project Structure

```text
Maze/
├── algorithms/               # Algorithm implementations
│   ├── Astar.py             # A* Search
│   ├── BFS.py               # Breadth-First Search
│   ├── DFS.py               # Depth-First Search
│   ├── IDS.py               # Iterative Deepening Search
│   ├── UCS.py               # Uniform Cost Search
│   ├── Greedy-search.py     # Greedy Best-First Search
│   ├── Hill_Climbing.py     # Hill Climbing
│   ├── sim_annealing.py     # Simulated Annealing
│   ├── Qlearning.py         # Q-Learning (Reinforcement Learning)
│   └── genetic_algo.py      # Genetic Algorithm
│
├── core/                    # Core maze and environment logic
│   ├── maze.py              # Maze generation and control
│   └── pyMaze.py            # Maze environment and data structures
│
├── utils/                   # Utilities and tools
│   ├── visuals.py           # Visualization utilities
│   └── performance.py       # Performance measurement and logging
│
├── AI_Report.pdf            # Detailed analysis and algorithm report
└── README.md                # Project documentation
```

---

## 🔍 Algorithms Implemented

### 🔹 Traditional Search

* **BFS** — Guarantees shortest path, complete
* **DFS** — Fast but not optimal or complete
* **UCS** — Optimal with cost, variant of Dijkstra’s
* **IDS** — Combines DFS space efficiency and BFS completeness
* **A**\* — Uses cost and heuristic (Manhattan distance)

### 🔹 Heuristic & Local Search

* **Greedy Best-First** — Fast but prone to suboptimal paths
* **Hill Climbing** — Simple local optimizer
* **Simulated Annealing** — Escapes local optima using probabilistic decisions

### 🔹 Machine Learning

* **Q-Learning** — Reinforcement learning with Q-table
* **Genetic Algorithm** — Evolutionary method for sequence optimization

---

## 🧠 Features

* ✅ Multiple Search and ML Algorithms
* 📈 Real-time Visualization
* 🧪 Performance Metrics and Comparisons
* 🧚 Evolutionary & Learning-based Solutions

---

## 🧹 Problem Setup

* **Grid**: 100×100 maze
* **Start**: Top-left corner `(1, 1)`
* **Goal**: Bottom-right corner `(100, 100)`
* **Actions**: N, S, E, W
* **Constraints**: Transitions blocked by walls

---

## 💻 Usage Examples

### ▶️ Run BFS (or any other search)

```python
from pyamaze import maze, agent
from BFS import bfs

m = maze()
m.CreateMaze()
path = bfs(m)

a = agent(m, footprints=True)
m.tracePath({a: path})
m.run()
```

### ▶️ Run Q-Learning

```python
from Qlearning import QLearningMaze
from pyamaze import maze

m = maze(20, 20)
m.CreateMaze()
q_agent = QLearningMaze(m, ['N', 'E', 'W', 'S'])
q_agent.train(episodes=1000)

policy = q_agent.get_policy()
path = q_agent.generate_path((1, 1), m._goal, policy)
```

### ▶️ Run Genetic Algorithm

```python
from genetic_algo import genetic_algorithm_maze
from pyamaze import maze

m = maze()
m.CreateMaze()
path = genetic_algorithm_maze(m, ['N', 'E', 'S', 'W'], f_thres=0, ngen=500, pmut=0.2)
```

---


## 📚 Report

Full details on algorithm design, evaluation, and results are documented.

---

## 🔧 Requirements

* Python 3.x
* Required packages:

  * `numpy`
  * `random`
  * `time`
  * `pyamaze`

Install with:

```bash
pip install -r requirements.txt
```

---




