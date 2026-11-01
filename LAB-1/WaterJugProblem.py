from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target):
    queue = deque([(0, 0)])
    visited = set()
    parent = {(0, 0): None}

    while queue:
        current = queue.popleft()

        if current in visited:
            continue

        visited.add(current)

        if current[0] == target or current[1] == target:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        x, y = current

        next_states = [
            (jug1_capacity, y),
            (x, jug2_capacity),
            (0, y),
            (x, 0),
            (min(x + y, jug1_capacity),
             y - min(x + y, jug1_capacity)),
            (x - min(x + y, jug2_capacity),
             min(x + y, jug2_capacity))
        ]

        for state in next_states:
            if state not in visited and state not in parent:
                parent[state] = current
                queue.append(state)

    return None


jug1 = 4
jug2 = 3
target = 2

solution = water_jug_problem(jug1, jug2, target)

if solution:
    print("Solution Path:")
    for state in solution:
        print(state)
else:
    print("No solution found.")