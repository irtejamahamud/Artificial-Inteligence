class IterativeDeepeningPath:
    def __init__(self):
        self.stack = []
        self.max_depth = 0
        self.goal_found = False
        self.path = []

    def iterative_deepening(self, graph, source, destination, node_names):
        self.number_of_nodes = len(graph)
        while not self.goal_found:
            print(f"\nPerforming depth-limited search with max depth: {self.max_depth}")
            self.depth_limited_search(graph, source, destination, node_names)
            self.max_depth += 1
        if self.goal_found:
            print(f"\nPath found from {source} to {destination} at depth {self.max_depth - 1}: {' -> '.join(self.path)}")
        else:
            print(f"\nNo path found from {source} to {destination}")

    def depth_limited_search(self, graph, source, goal, node_names):
        self.stack = [(source, 0, [source])]
        visited = set()
        while self.stack:
            element, depth, path = self.stack.pop()
            if element not in visited:
                visited.add(element)
                if element == goal:
                    self.goal_found = True
                    self.path = path
                    return
                if depth < self.max_depth:
                    element_index = node_names.index(element)
                    for i, is_neighbor in enumerate(graph[element_index]):
                        if is_neighbor == 1:
                            neighbor = node_names[i]
                            self.stack.append((neighbor, depth + 1, path + [neighbor]))

if __name__ == "__main__":
    try:
        number_of_nodes = int(input("Enter the number of nodes in the graph: "))
        print("Enter the adjacency matrix row by row:")
        graph = []
        for _ in range(number_of_nodes):
            row = list(map(int, input().split()))
            graph.append(row)
        
        node_names = [str(i+1) for i in range(number_of_nodes)]
        
        source = input("Enter the source node: ").strip()
        destination = input("Enter the destination node: ").strip()
        
        if source not in node_names or destination not in node_names:
            raise ValueError("Source or destination node not in graph")

        iterative_deepening_path = IterativeDeepeningPath()
        iterative_deepening_path.iterative_deepening(graph, source, destination, node_names)
    except ValueError:
        print("Wrong input format")
