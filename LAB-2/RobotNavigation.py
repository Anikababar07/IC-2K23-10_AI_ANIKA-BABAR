from collections import deque

def robot_navigation(grid, start, goal):

    rows = len(grid)
    cols = len(grid[0])

    queue = deque([(start, [start])])
    visited = {start}

    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (0, -1),  # Left
        (-1, 0)   # Up
    ]

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        for dr, dc in directions:
            r = current[0] + dr
            c = current[1] + dc
            next_position = (r, c)

            if (0 <= r < rows and
                0 <= c < cols and
                grid[r][c] == 0 and
                next_position not in visited):

                visited.add(next_position)
                queue.append((next_position, path + [next_position]))

    return None


grid = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = robot_navigation(grid, start, goal)

if path:
    print("Robot Navigation Path:")
    for position in path:
        print(position)
else:
    print("No path found!")