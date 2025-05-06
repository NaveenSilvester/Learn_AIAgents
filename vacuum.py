class VacuumAgent:
    def __init__(self):
        # Internal state: tracks cleanliness of rooms
        self.state = {'A': 'Unknown', 'B': 'Unknown'}
        # Current location of the agent
        self.location = 'A'

    def update_state(self, percept):
        # Percept: {'location': 'A' or 'B', 'status': 'Dirty' or 'Clean'}
        self.location = percept['location']
        self.state[self.location] = percept['status']

    def choose_action(self):
        # Rule-based decision making
        if self.state[self.location] == 'Dirty':
            return 'Suck'
        elif self.location == 'A' and self.state['B'] == 'Dirty':
            return 'Move Right'
        elif self.location == 'B' and self.state['A'] == 'Dirty':
            return 'Move Left'
        else:
            return 'NoOp'  # Do nothing if both rooms are clean or unknown

    def act(self, percept):
        # Update state and choose action
        self.update_state(percept)
        action = self.choose_action()
        return action

# Simulate the environment and agent
def simulate_vacuum():
    agent = VacuumAgent()
    # Example sequence of percepts
    percepts = [
        {'location': 'A', 'status': 'Dirty'},  # Room A is dirty
        {'location': 'A', 'status': 'Clean'},  # After sucking, A is clean
        {'location': 'B', 'status': 'Dirty'},  # Move to B, B is dirty
        {'location': 'B', 'status': 'Clean'},  # After sucking, B is clean
    ]

    print("Initial state:", agent.state)
    for percept in percepts:
        action = agent.act(percept)
        print(f"Percept: {percept}, Action: {action}, State: {agent.state}")

# Run the simulation
simulate_vacuum()
