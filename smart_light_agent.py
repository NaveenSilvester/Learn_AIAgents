import random
import time
# Simple reflex agent function
def simple_reflex_light_agent(light_level):
    if light_level < 100:
        return "Turn Light ON"
    else:
        return "Turn Light OFF"

# Simulate the environment and agent loop
def main():
    print("Smart Light Bulb Agent Simulation")
    print("--------------------------------")
    
    while True:
        # Simulate sensor reading (random light level between 0 and 200 lux)
        light_level = random.randint(0, 200)
        
        # Get action from the agent
        action = simple_reflex_light_agent(light_level)
        
        # Display the result
        print(f"Light Level: {light_level} lux | Action: {action}")
        
        # Wait for a second before the next reading
        time.sleep(1)
        
        # Optional: Break the loop after a few iterations for demo purposes
        # Remove this for continuous operation
        if input("Continue? (y/n): ").lower() == 'n':
            break

# Run the simulation
if __name__ == "__main__":
    main()
