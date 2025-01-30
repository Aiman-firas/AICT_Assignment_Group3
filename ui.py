from algorithms.bfs import bfs_shortest_path
from algorithms.dfs import dfs_shortest_path
from algorithms.gbfs import gbfs_shortest_path
from algorithms.astar import astar_shortest_path
import time
import matplotlib.pyplot as plt

# Heuristic for GBFS and A*
heuristic = {
    'A': 10, 'B': 8, 'C': 7, 'D': 5, 'E': 6,
    'F': 4, 'G': 2, 'H': 3, 'I': 4, 'J': 0
}

# Measure runtime and run algorithm
def measure_performance(algorithm, graph, start, goal):
    start_time = time.perf_counter()
    if algorithm == "GBFS":
        path = gbfs_shortest_path(graph, start, goal, heuristic)
    elif algorithm == "A*":
        path = astar_shortest_path(graph, start, goal, heuristic)
    else:
        path = algorithm(graph, start, goal)
    runtime = time.perf_counter() - start_time
    return path, runtime

# Visualize runtime performance
def visualize_performance(results):
    algorithms = [r[0] for r in results]
    runtimes = [r[2] for r in results]

    plt.bar(algorithms, runtimes)
    plt.title("Algorithm Runtime Comparison")
    plt.xlabel("Algorithm")
    plt.ylabel("Runtime (seconds)")
    plt.show()

# Compare all algorithms and display results
def compare_algorithms(graph, start, goal):
    algorithms = {
        "BFS": bfs_shortest_path,
        "DFS": dfs_shortest_path,
        "GBFS": "GBFS",
        "A*": "A*"
    }
    results = []

    for name, algo in algorithms.items():
        path, runtime = measure_performance(algo, graph, start, goal)
        results.append((name, path, runtime))

    print("\nPerformance Comparison:")
    for algo, path, runtime in results:
        print(f"{algo}: Path = {path}, Runtime = {runtime:.6f} seconds")

    visualize_performance(results)

# User interface for selecting nodes and algorithms
def run_ui(city_map, choose_algorithm):
    print("Welcome to the Intelligent Transportation System")
    print("Available locations:", ", ".join(city_map.keys()))

    start = input("\nEnter start location: ").strip()
    while start not in city_map:
        print("Invalid location. Try again.")
        start = input("Enter start location: ").strip()

    goal = input("Enter end location: ").strip()
    while goal not in city_map:
        print("Invalid location. Try again.")
        goal = input("Enter end location: ").strip()

    print("\nChoose a search algorithm:")
    print("1. Breadth-First Search (BFS)")
    print("2. Depth-First Search (DFS)")
    print("3. Greedy Best-First Search (GBFS)")
    print("4. A* Search")
    print("5. Compare all algorithms for this start and end location")
    algo_choice = input("Enter your choice (1-5): ").strip()

    algorithms = {
        "1": "BFS",
        "2": "DFS",
        "3": "GBFS",
        "4": "A*"
    }

    if algo_choice in algorithms:
        algorithm = algorithms[algo_choice]
        print(f"\nRunning {algorithm}...")
        path = choose_algorithm(algorithm, city_map, start, goal)
        if path:
            print(f"Shortest path from {start} to {goal}: {' -> '.join(path)}")
        else:
            print(f"No path found from {start} to {goal}.")
    elif algo_choice == "5":
        print("\nComparing all algorithms for this start and end location...")
        compare_algorithms(city_map, start, goal)
    else:
        print("Invalid choice. Returning to the main menu.")
