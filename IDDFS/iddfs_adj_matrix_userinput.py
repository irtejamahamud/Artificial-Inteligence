class IterativeDeepening:
    def __init__(self):
        self.stack = []
        self.number_of_nodes = 0
        self.depth = 0
        self.max_depth = 0
        self.goal_found = False

    def iterative_deepening(self, graph, destination, node_names):
        self.number_of_nodes = len(graph)
        while not self.goal_found:
            print(f"\nPerforming depth-limited search with max depth: {self.max_depth}")
            self.depth_limited_search(graph, node_names[0], destination, node_names)
            self.max_depth += 1
        print(f"\nGoal Found at depth {self.depth}")

    def depth_limited_search(self, graph, source, goal, node_names):
        self.stack = [(source, 0)]
        visited = set()
        print(f"\nAt Depth {self.max_depth}")
        while self.stack:
            element, depth = self.stack.pop()
            if element not in visited:
                visited.add(element)
                print(element, end=' ')
                if element == goal:
                    self.goal_found = True
                    self.depth = depth
                    return
                if depth < self.max_depth:
                    element_index = node_names.index(element)
                    for i, is_neighbor in enumerate(graph[element_index]):
                        if is_neighbor == 1:
                            neighbor = node_names[i]
                            self.stack.append((neighbor, depth + 1))

if __name__ == "__main__":
    try:
        number_of_nodes = int(input("Enter the number of nodes in the graph: "))
        print("Enter the adjacency matrix row by row:")
        graph = []
        for _ in range(number_of_nodes):
            row = list(map(int, input().split()))
            graph.append(row)
        
        node_names = [str(i+1) for i in range(number_of_nodes)]

        destination = input("Enter the destination for the graph: ").strip()
        if destination not in node_names:
            raise ValueError("Destination node not in graph")

        iterative_deepening = IterativeDeepening()
        iterative_deepening.iterative_deepening(graph, destination, node_names)
    except ValueError:
        print("Wrong input format")
