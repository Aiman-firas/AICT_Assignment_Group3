# main.py

from collections import deque

# Step 1: Represent the graph (city map)
city_map = {
    'A': {'B': 3, 'C': 5},
    'B': {'A': 3, 'D': 2, 'E': 7},
    'C': {'A': 5, 'D': 4},
    'D': {'B': 2, 'C': 4, 'E': 6},
    'E': {'B': 7, 'D': 6}
}

# Step 2: BFS Algorithm
def bfs_shortest_path(graph, start, goal):
    # Queue to store (current_node, path_to_node)
    queue = deque([(start, [start])])
    visited = set()
    
    while queue:
        current_node, path = queue.popleft()
        
        if current_node == goal:
            return path  # Found the shortest path
        
        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None  # No path found

# Step 3: Test BFS
if __name__ == "__main__":
    start = 'A'
    goal = 'E'
    path = bfs_shortest_path(city_map, start, goal)
    print(f"Shortest path from {start} to {goal}: {path}")
