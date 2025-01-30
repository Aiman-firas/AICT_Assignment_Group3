from collections import deque

def bfs_shortest_path(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current_node, path = queue.popleft()

        if current_node == goal:
            return path

        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph[current_node]:
                queue.append((neighbor, path + [neighbor]))

    return None  # No path found
