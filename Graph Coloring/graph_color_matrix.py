def graph_coloring(graph, num_of_colors):
    V = len(graph)
    colors = [0] * V

    def solve(v):
        if v == V:
            raise Exception("Solution found")
        for c in range(1, num_of_colors + 1):
            if is_possible(v, c):
                colors[v] = c
                solve(v + 1)
                colors[v] = 0

    def is_possible(v, c):
        for i in range(V):
            if graph[v][i] == 1 and c == colors[i]:
                return False
        return True

    def display():
        text_color = ["", "RED", "GREEN", "BLUE", "YELLOW", "ORANGE", "PINK",
                      "BLACK", "BROWN", "WHITE", "PURPLE", "VIOLET"]
        print("Colors: ", end="")
        for i in range(V):
            print(text_color[colors[i]], end=" ")

    try:
        solve(0)
        print("No solution")
    except Exception as e:
        print("\nSolution exists")
        display()


print("Graph Coloring Algorithm Test")

V = int(input("Enter number of vertices: "))
print("\nEnter matrix (separate elements by space, rows by newline):")
graph = []
for _ in range(V):
    row = list(map(int, input().split()))
    graph.append(row)

num_colors = int(input("\nEnter number of colors: "))

graph_coloring(graph, num_colors)

# 0 1 1 0 0 0 0
# 1 0 1 1 0 0 0
# 1 1 0 1 1 1 0
# 0 1 1 0 1 0 0
# 0 0 1 1 0 1 0
# 0 0 1 0 1 0 0
# 0 0 0 0 0 0 0