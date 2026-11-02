from collections import deque

def solve_maze(maze, start, goal):
    rows = len(maze)
    cols = len(maze[0])

    queue = deque([(start, [start])])
    visited = set([start])

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

        for direction in directions:
            new_row = current[0] + direction[0]
            new_col = current[1] + direction[1]
            next_position = (new_row, new_col)

            if (0 <= new_row < rows and
                0 <= new_col < cols and
                maze[new_row][new_col] == 0 and
                next_position not in visited):

                visited.add(next_position)
                queue.append((next_position, path + [next_position]))

    return None


maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)

path = solve_maze(maze, start, goal)

if path:
    print("Path found:")
    for position in path:
        print(position)
else:
    print("No path found!")