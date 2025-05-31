from pyamaze import maze, agent
import random
import time

class QLearningMaze:
    def __init__(self, maze, actions, learning_rate=0.1, discount_factor=0.9, epsilon=0.2):
        self.maze = maze
        self.actions = actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.q_table = self.initialize_q_table()

    def initialize_q_table(self):
        q_table = {}
        for cell in self.maze.maze_map.keys():
            q_table[cell] = {action: 0.0 for action in self.actions}
        return q_table

    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(self.actions)  # Explore
        else:
            return max(self.q_table[state], key=self.q_table[state].get)  # Exploit

    def update_q_value(self, state, action, reward, next_state):
        max_future_q = max(self.q_table[next_state].values()) if next_state in self.q_table else 0
        current_q = self.q_table[state][action]
        self.q_table[state][action] = current_q + self.learning_rate * (reward + self.discount_factor * max_future_q - current_q)

    def take_action(self, state, action):
        if self.maze.maze_map[state][action]:
            if action == 'N':
                next_state = (state[0] - 1, state[1])
            elif action == 'E':
                next_state = (state[0], state[1] + 1)
            elif action == 'W':
                next_state = (state[0], state[1] - 1)
            elif action == 'S':
                next_state = (state[0] + 1, state[1])
            else:
                next_state = state
            reward = 1 if next_state == self.maze._goal else -0.04
        else:
            next_state = state
            reward = -1  # Penalty for invalid action
        return next_state, reward

    def train(self, episodes, max_steps=200):
        for episode in range(episodes):
            state = (self.maze.rows, self.maze.cols)  # Start at the bottom-right corner
            steps = 0

            while state != self.maze._goal and steps < max_steps:
                action = self.choose_action(state)
                next_state, reward = self.take_action(state, action)
                self.update_q_value(state, action, reward, next_state)
                state = next_state
                steps += 1

    def get_policy(self):
        policy = {}
        for state in self.q_table:
            policy[state] = max(self.q_table[state], key=self.q_table[state].get)
        return policy

    def generate_path(self, start, goal, policy):
        path = []
        current_state = start
        while current_state != goal:
            action = policy[current_state]
            if action == 'N':
                next_state = (current_state[0] - 1, current_state[1])
            elif action == 'E':
                next_state = (current_state[0], current_state[1] + 1)
            elif action == 'W':
                next_state = (current_state[0], current_state[1] - 1)
            elif action == 'S':
                next_state = (current_state[0] + 1, current_state[1])
            path.append(next_state)
            current_state = next_state
        return path

# Load the maze
m = maze(20, 20)
m.CreateMaze(loadMaze='maze--2024-12-30--18-30-59.csv')  # Load your maze

# Define possible actions
actions = ['N', 'E', 'W', 'S']

# Create Q-learning agent
q_learning_agent = QLearningMaze(m, actions, learning_rate=0.1, discount_factor=0.9, epsilon=0.1)
q_learning_agent.train(episodes=500)  # Train for more episodes

# Generate the agent's path using the policy
policy = q_learning_agent.get_policy()
start = (m.rows, m.cols)  # Bottom-right corner
goal = m._goal           # Top-left corner or specified goal
path = q_learning_agent.generate_path(start, goal, policy)

# Visualize the path on the maze
a = agent(m, footprints=True, filled=True, shape='arrow')  # Create an agent
m.tracePath({a: path})  # Trace the path
m.run()  # Display the maze and agent's movement
