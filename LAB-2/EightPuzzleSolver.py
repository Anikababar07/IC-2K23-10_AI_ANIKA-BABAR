from collections import deque

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)

    row, col = divmod(zero, 3)

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_position = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_position] = (
                new_state[new_position],
                new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


def solve_puzzle(start, goal):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None


start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

solution = solve_puzzle(start, goal)

if solution:
    print("Solution Found!")
    print("Total Moves:", len(solution) - 1)

    for step, state in enumerate(solution):
        print("\nStep", step)
        for i in range(0, 9, 3):
            print(state[i:i+3])
else:
    print("No Solution Found!")