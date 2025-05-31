import numpy as np
import random
import json
import time
from pyamaze import maze, agent


class QLearningMaze:
    def __init__(self, maze, actions, learning_rate=0.1, discount_factor=0.9, epsilon=0.1):
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
        self.q_table[state][action] = current_q + self.learning_rate * (
            reward + self.discount_factor * max_future_q - current_q
        )

    def calculate_proximity_reward(self, state, goal):
        # Reward for moving closer to the goal based on Manhattan distance
        return -0.04 + (1 / (1 + abs(state[0] - goal[0]) + abs(state[1] - goal[1])))

    def take_action(self, state, action):
        if self.maze.maze_map[state][action]:  # Check if the move is valid
            if action == 'N':
                next_state = (state[0] - 1, state[1])
            elif action == 'E':
                next_state = (state[0], state[1] + 1)
            elif action == 'W':
                next_state = (state[0], state[1] - 1)
            elif action == 'S':
                next_state = (state[0] + 1, state[1])
            reward = 1 if next_state == self.maze._goal else self.calculate_proximity_reward(next_state, self.maze._goal)
        else:
            next_state = state  # Stay in place for an invalid move
            reward = -1  # Penalty for hitting a wall
        return next_state, reward

    def train(self, episodes, max_steps=500):
        for episode in range(episodes):
            state = (1, 1)  # Starting position (bottom-left corner)
            for step in range(max_steps):
                action = self.choose_action(state)
                next_state, reward = self.take_action(state, action)
                self.update_q_value(state, action, reward, next_state)
                state = next_state
                if state == self.maze._goal:  # Goal reached
                    break

    def get_policy(self):
        policy = {}
        for state, actions in self.q_table.items():
            best_action = max(actions, key=actions.get)
            policy[state] = best_action
        return policy

    def generate_path(self, start, goal, policy, max_steps=500):
        path = [start]
        state = start
        for _ in range(max_steps):
            action = policy.get(state)
            if not action:
                break  # No valid action found
            next_state, _ = self.take_action(state, action)
            if next_state == state:
                break  # No progress, stop to prevent infinite loop
            path.append(next_state)
            state = next_state
            if state == goal:
                break
        return path


# Define the maze
m = maze(20, 20)
m.CreateMaze(x=20, y=20)  # Goal position (top-left corner)

# Define possible actions
actions = ['N', 'E', 'W', 'S']

# Create Q-learning agent
q_learning_agent = QLearningMaze(m, actions, learning_rate=0.5, discount_factor=0.95, epsilon=0.1)
q_learning_agent.train(episodes=1000, max_steps=500)

# Get the learned policy
policy = q_learning_agent.get_policy()

# Generate the agent's path using the policy
start = (1, 1)  # Start position (bottom-left corner)
goal = (20, 20)  # Goal position (top-left corner)
path = q_learning_agent.generate_path(start, goal, policy)

# Visualize the policy-based path using pyamaze
a = agent(m, footprints=True, filled=True, shape='arrow')
m.tracePath({a: path})
m.run()
