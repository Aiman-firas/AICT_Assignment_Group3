import heapq

def gbfs_shortest_path(graph, start, goal, heuristic):
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        _, current_node, path = heapq.heappop(queue)

        if current_node == goal:
            return path

        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph[current_node]:
                heapq.heappush(queue, (heuristic[neighbor], neighbor, path + [neighbor]))

    return None
