def run_ui(city_map, choose_algorithm):
    print("Welcome to the Intelligent Transportation System")
    print("Available locations:", ", ".join(city_map.keys()))

    start = input("Enter start location: ").strip()
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
    algo_choice = input("Enter your choice (1-4): ").strip()

    algorithms = {
        "1": "BFS",
        "2": "DFS",
        "3": "GBFS",
        "4": "A*"
    }

    algorithm = algorithms.get(algo_choice)
    if not algorithm:
        print("Invalid choice. Exiting.")
        return

    print(f"\nRunning {algorithm}...")
    path = choose_algorithm(algorithm, city_map, start, goal)
    if path:
        print(f"Shortest path from {start} to {goal}: {' -> '.join(path)}")
    else:
        print(f"No path found from {start} to {goal}.")
