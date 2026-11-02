# State Space Representation using a Graph

state_space = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("State Space Representation:\n")

for state, next_states in state_space.items():
    print(f"State {state} -> {next_states}")

print("\nInitial State: A")
print("Goal State: F")