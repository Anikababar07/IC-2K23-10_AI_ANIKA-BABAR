from collections import deque

def is_valid(state):
    missionaries_left, cannibals_left, boat = state
    missionaries_right = 3 - missionaries_left
    cannibals_right = 3 - cannibals_left

    # Check valid number of missionaries and cannibals
    if not (0 <= missionaries_left <= 3 and 0 <= cannibals_left <= 3):
        return False

    # Missionaries should not be outnumbered by cannibals
    if missionaries_left > 0 and missionaries_left < cannibals_left:
        return False

    if missionaries_right > 0 and missionaries_right < cannibals_right:
        return False

    return True


def get_next_states(state):
    missionaries_left, cannibals_left, boat = state

    moves = [
        (1, 0), (2, 0),
        (0, 1), (0, 2),
        (1, 1)
    ]

    next_states = []

    for missionaries, cannibals in moves:
        if boat == 1:
            new_state = (
                missionaries_left - missionaries,
                cannibals_left - cannibals,
                0
            )
        else:
            new_state = (
                missionaries_left + missionaries,
                cannibals_left + cannibals,
                1
            )

        if is_valid(new_state):
            next_states.append(new_state)

    return next_states


def solve():
    initial_state = (3, 3, 1)
    goal_state = (0, 0, 0)

    queue = deque([(initial_state, [initial_state])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path

        if current_state in visited:
            continue

        visited.add(current_state)

        for next_state in get_next_states(current_state):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))

    return None


solution = solve()

if solution:
    print("Solution found:")
    print("State format: (Missionaries Left, Cannibals Left, Boat)")
    print("Boat: 1 = Left side, 0 = Right side\n")

    for step, state in enumerate(solution):
        print(f"Step {step}: {state}")
else:
    print("No solution found.")