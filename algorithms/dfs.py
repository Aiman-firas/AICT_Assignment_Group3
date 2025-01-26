def dfs_shortest_path(graph, start, goal, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()

    if start == goal:
        return path

    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs_shortest_path(graph, neighbor, goal, path + [neighbor], visited)
            if result:
                return result

    return None
