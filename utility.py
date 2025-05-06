import random

class VacuumAgent:
    def __init__(self, grid_size=3, battery=20):
        self.grid_size = grid_size
        self.position = [0, 0]  # Starting at (0,0)
        self.battery = battery
        self.direction = 'up'  # Possible: up, right, down, left
        # Grid: 0 = clean, 1 = dirty
        self.grid = [[random.choice([0, 1]) for _ in range(grid_size)] for _ in range(grid_size)]
        self.grid[0][0] = 0  # Starting position is clean
        self.total_utility = 0

    def is_valid_position(self, pos):
        return 0 <= pos[0] < self.grid_size and 0 <= pos[1] < self.grid_size

    def get_next_position(self):
        if self.direction == 'up':
            return [self.position[0] - 1, self.position[1]]
        elif self.direction == 'right':
            return [self.position[0], self.position[1] + 1]
        elif self.direction == 'down':
            return [self.position[0] + 1, self.position[1]]
        elif self.direction == 'left':
            return [self.position[0], self.position[1] - 1]

    def calculate_utility(self, action):
        utility = -1  # Battery cost for any action
        if action == 'clean' and self.grid[self.position[0]][self.position[1]] == 1:
            utility += 10  # Reward for cleaning dirt
        elif action == 'move':
            next_pos = self.get_next_position()
            if not self.is_valid_position(next_pos):
                utility -= 50  # Penalty for hitting a wall
        return utility

    def choose_action(self):
        actions = ['move', 'clean', 'turn_left', 'turn_right']
        utilities = [self.calculate_utility(action) for action in actions]
        max_utility = max(utilities)
        best_actions = [actions[i] for i in range(len(actions)) if utilities[i] == max_utility]
        return random.choice(best_actions)  # Randomly pick among best actions

    def perform_action(self, action):
        if self.battery <= 0:
            print("Battery depleted!")
            return False

        self.battery -= 1
        if action == 'clean' and self.grid[self.position[0]][self.position[1]] == 1:
            self.grid[self.position[0]][self.position[1]] = 0
            self.total_utility += 10
            print(f"Cleaned at {self.position}, Utility: +10")
        elif action == 'move':
            next_pos = self.get_next_position()
            if self.is_valid_position(next_pos):
                self.position = next_pos
                print(f"Moved to {self.position}")
            else:
                self.total_utility -= 50
                print(f"Hit wall at {self.position}, Utility: -50")
        elif action == 'turn_left':
            directions = ['up', 'left', 'down', 'right']
            self.direction = directions[(directions.index(self.direction) + 1) % 4]
            print(f"Turned left, facing {self.direction}")
        elif action == 'turn_right':
            directions = ['up', 'right', 'down', 'left']
            self.direction = directions[(directions.index(self.direction) + 1) % 4]
            print(f"Turned right, facing {self.direction}")
        self.total_utility -= 1  # Battery cost
        return True

    def display_grid(self):
        for i in range(self.grid_size):
            row = ''
            for j in range(self.grid_size):
                if [i, j] == self.position:
                    row += 'V '
                else:
                    row += str(self.grid[i][j]) + ' '
            print(row)
        print(f"Battery: {self.battery}, Total Utility: {self.total_utility}")

# Simulate the agent
agent = VacuumAgent()
steps = 10
for _ in range(steps):
    agent.display_grid()
    if agent.battery <= 0:
        break
    action = agent.choose_action()
    print(f"Chosen action: {action}")
    agent.perform_action(action)
    print("-" * 20)