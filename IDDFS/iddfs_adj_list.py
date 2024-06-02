class IterativeDeepening:
    def __init__(self):
        self.stack = []
        self.number_of_nodes = 0
        self.depth = 0
        self.max_depth = 0
        self.goal_found = False

    def iterative_deepening(self, graph, destination):
        self.number_of_nodes = len(graph)
        while not self.goal_found:
            self.depth_limited_search(graph, 'A', destination)
            self.max_depth += 1
        print("\nGoal Found at depth", self.depth)

    def depth_limited_search(self, graph, source, goal):
        visited = {}
        self.stack.append((source, 0))
        print("\nAt Depth", self.max_depth)
        print(source, end='\t')
        while self.stack:
            element, depth = self.stack.pop()
            if depth <= self.max_depth:
                for neighbor in graph[element]:
                    self.stack.append((neighbor, depth + 1))
                    print(neighbor, end='\t')
                    if neighbor == goal:
                        self.goal_found = True
                        self.depth = depth + 1
                        return

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['E', 'F'],
        'C': ['G'],
        'D': ['H'],
        'E': ['I'],
        'F': ['J', 'K'],
        'G': ['L'],
        'H': ['M', 'N'],
        'I': [],
        'J': [],
        'K': [],
        'L': [],
        'M': [],
        'N': []
    }
    try:
        print("Enter the destination for the graph")
        destination = input().upper()
        iterative_deepening = IterativeDeepening()
        iterative_deepening.iterative_deepening(graph, destination)
    except ValueError:
        print("Wrong Input format")
