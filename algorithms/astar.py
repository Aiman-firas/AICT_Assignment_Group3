import heapq

def astar_shortest_path(graph, start, goal, heuristic):
    queue = [(0, start, [start], 0)]
    visited = set()

    while queue:
        _, current_node, path, g_cost = heapq.heappop(queue)

        if current_node == goal:
            return path

        if current_node not in visited:
            visited.add(current_node)
            for neighbor, weight in graph[current_node].items():
                f_cost = g_cost + weight + heuristic[neighbor]
                heapq.heappush(queue, (f_cost, neighbor, path + [neighbor], g_cost + weight))

    return None
