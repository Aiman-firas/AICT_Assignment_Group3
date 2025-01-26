from data.city_map import city_map
from algorithms.bfs import bfs_shortest_path
from algorithms.dfs import dfs_shortest_path
from algorithms.gbfs import gbfs_shortest_path
from algorithms.astar import astar_shortest_path

heuristic = {
    'A': 10, 'B': 8, 'C': 7, 'D': 5, 'E': 6,
    'F': 4, 'G': 2, 'H': 3, 'I': 4, 'J': 0
}

def choose_algorithm(algorithm, graph, start, goal):
    if algorithm == "BFS":
        return bfs_shortest_path(graph, start, goal)
    elif algorithm == "DFS":
        return dfs_shortest_path(graph, start, goal)
    elif algorithm == "GBFS":
        return gbfs_shortest_path(graph, start, goal, heuristic)
    elif algorithm == "A*":
        return astar_shortest_path(graph, start, goal, heuristic)
    else:
        raise ValueError("Invalid algorithm selected.")

if __name__ == "__main__":
    from ui import run_ui
    run_ui(city_map, choose_algorithm)
