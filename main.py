from data.city_map import city_map
from ui import run_ui

# Main program loop
if __name__ == "__main__":
    while True:
        print("\nSelect an option:")
        print("1. Run User Interface (choose start/end nodes and algorithm)")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "1":
            run_ui(city_map, lambda algo, graph, start, goal: {
                "BFS": bfs_shortest_path(graph, start, goal),
                "DFS": dfs_shortest_path(graph, start, goal),
                "GBFS": gbfs_shortest_path(graph, start, goal, heuristic),
                "A*": astar_shortest_path(graph, start, goal, heuristic)
            }[algo])
        elif choice == "2":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
