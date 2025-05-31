import matplotlib.pyplot as plt
import seaborn as sns
import json

# Load Q-table snapshots
with open('q_table_snapshots.json', 'r') as f:
    snapshots = json.load(f)

for episode, q_table in snapshots.items():
    heatmap_data = []
    for state, actions in q_table.items():
        row = [actions['N'], actions['E'], actions['W'], actions['S']]
        heatmap_data.append(row)

    plt.figure(figsize=(10, 6))
    sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', xticklabels=['N', 'E', 'W', 'S'])
    plt.title(f"Q-Value Heatmap at Episode {episode}")
    plt.xlabel("Actions")
    plt.ylabel("States")
    plt.show()
#========================
import matplotlib.pyplot as plt

# Load steps per episode
with open('steps_per_episode.csv', 'r') as f:
    steps = list(map(int, f.read().split(',')))

# Calculate running average
averages = [sum(steps[:i+1])/(i+1) for i in range(len(steps))]

plt.figure(figsize=(10, 6))
plt.plot(range(len(steps)), averages, label="Average Steps")
plt.xlabel("Episodes")
plt.ylabel("Average Steps")
plt.title("Average Steps to Reach Goal Over Episodes")
plt.legend()
plt.grid(True)
plt.show()
#=============
# Load success rate data
with open('success_rate.csv', 'r') as f:
    success = list(map(int, f.read().split(',')))

cumulative_success = [sum(success[:i+1])/(i+1) for i in range(len(success))]

plt.figure(figsize=(10, 6))
plt.plot(range(len(success)), cumulative_success, label="Success Rate")
plt.xlabel("Episodes")
plt.ylabel("Success Rate")
plt.title("Success Rate Progression Over Episodes")
plt.legend()
plt.grid(True)
plt.show()
