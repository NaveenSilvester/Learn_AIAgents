from collections import deque

# Define the maze (0 = open, 1 = wall)
maze = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]

# Define start and goal positions
start = (0, 0)  # (row, col)
goal = (4, 4)

# Possible actions: up, right, down, left
actions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
action_names = ['Up', 'Right', 'Down', 'Left']

# Goal-Based Agent using BFS
def goal_based_agent(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    
    # Check if position is valid
    def is_valid(pos):
        r, c = pos
        return 0 <= r < rows and 0 <= c < cols and maze[r][c] == 0
    
    # BFS to find the shortest path
    queue = deque([(start, [])])  # (position, path)
    visited = set([start])
    
    while queue:
        (current_r, current_c), path = queue.popleft()
        
        # Check if goal is reached
        if (current_r, current_c) == goal:
            return path
        
        # Explore possible actions
        for i, (dr, dc) in enumerate(actions):
            next_r, next_c = current_r + dr, current_c + dc
            next_pos = (next_r, next_c)
            
            if is_valid(next_pos) and next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, path + [action_names[i]]))
    
    return None  # No path found

# Run the agent
path = goal_based_agent(maze, start, goal)
if path:
    print("Path to goal:", path)
else:
    print("No path found!")

# Simulate the agent's movement
def simulate_movement(maze, start, path):
    current = start
    print("Starting at:", current)
    for action in path:
        if action == 'Up':
            current = (current[0] - 1, current[1])
        elif action == 'Right':
            current = (current[0], current[1] + 1)
        elif action == 'Down':
            current = (current[0] + 1, current[1])
        elif action == 'Left':
            current = (current[0], current[1] - 1)
        print(f"Move {action} to: {current}")

if path:
    simulate_movement(maze, start, path)
