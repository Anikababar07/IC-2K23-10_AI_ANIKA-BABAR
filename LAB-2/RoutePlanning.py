import heapq

def dijkstra(graph, start, goal):
    priority_queue = [(0, start)]
    visited = set()
    distances = {start: 0}
    previous = {}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            break

        for neighbor, distance in graph[current_node].items():
            new_distance = current_distance + distance

            if neighbor not in distances or new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node
                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    path = []

    if goal in distances:
        current = goal

        while current != start:
            path.append(current)
            current = previous[current]

        path.append(start)
        path.reverse()

        return distances[goal], path

    return None, []


graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}

start = 'A'
goal = 'E'

distance, path = dijkstra(graph, start, goal)

print("Shortest Distance:", distance)
print("Best Route:", " -> ".join(path))