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
            print("\nPerforming depth-limited search with max depth:", self.max_depth)
            self.depth_limited_search(graph, 'A', destination, node_names)
            self.max_depth += 1
        print("\nGoal found at depth", self.depth)

    def depth_limited_search(self, graph, source, goal, node_names):
        self.stack = [(source, 0)]
        visited = set()
        while self.stack:
            element, depth = self.stack.pop()
            if element not in visited:
                visited.add(element)
                print(element, end='\t')
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
    # Adjacency matrix for the graph
    graph = [
        # A  B  C  D  E  F  G  H  I  J  K  L  M  N
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # A
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], # B
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], # C
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], # D
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], # E
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], # F
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], # G
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], # H
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # I
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # J
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # K
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # L
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # M
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # N
    ]

    node_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']

    try:
        destination = input("Enter the destination for the graph: ").upper()
        iterative_deepening = IterativeDeepening()
        iterative_deepening.iterative_deepening(graph, destination, node_names)
    except ValueError:
        print("Wrong input format")
