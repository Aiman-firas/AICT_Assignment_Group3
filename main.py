import sys
import os

# Ensure the project root is added to sys.path (helps Python recognize modules)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data.city_map import city_map
from ui import run_ui

# Fix imports by adding `algorithms.` explicitly
from algorithms.bfs import bfs_shortest_path
from algorithms.dfs import dfs_shortest_path
from algorithms.gbfs import gbfs_shortest_path
from algorithms.astar import astar_shortest_path

# Heuristic for GBFS and A*
heuristic = {
    'A': 10, 'B': 8, 'C': 7, 'D': 5, 'E': 6,
    'F': 4, 'G': 2, 'H': 3, 'I': 4, 'J': 0
}

# Main program loop
if __name__ == "__main__":
    while True:
        print("\nSelect an option:")
        print("1. Run User Interface (choose start/end nodes and algorithm)")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "1":
            run_ui(city_map, lambda algo, graph, start, goal: {
                "BFS": bfs_shortest_path,
                "DFS": dfs_shortest_path,
                "GBFS": lambda g, s, e: gbfs_shortest_path(g, s, e, heuristic),
                "A*": lambda g, s, e: astar_shortest_path(g, s, e, heuristic)
            }[algo](graph, start, goal))
        elif choice == "2":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
