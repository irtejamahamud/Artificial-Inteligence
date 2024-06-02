def graph_coloring(adj_list, num_of_colors):
    V = len(adj_list)
    colors = [0] * V  # Initialize colors for each vertex

    def solve(v):
        if v == V:
            raise Exception("Solution found")
        for c in range(1, num_of_colors + 1):
            if is_possible(v, c):
                colors[v] = c
                solve(v + 1)
                colors[v] = 0

    def is_possible(v, c):
        for neighbor in adj_list[v]:
            if colors[neighbor] == c:
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


# Main function
print("Graph Coloring Algorithm Test")

# Given adjacency list
adj_list = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3, 4, 5],
    3: [1, 2, 4],
    4: [2, 3, 5],
    5: [2, 4],
    6: []
}

# Accept number of colors
num_colors = int(input("\nEnter number of colors: "))

# Call graph_coloring function
graph_coloring(adj_list, num_colors)