from collections import deque

def print_direction(m, x, y):
    directions = ["Down", "Up", "Right", "Left"]
    print(f"Moving {directions[m]} ({x}, {y})")

def bfs(graph, source, directions, x_move, y_move, N, goal):
    queue = deque([(source, 0)])  # Include move count in the queue
    visited = set([source])
    path = {source: None}

    while queue:
        (u_x, u_y), move_count = queue.popleft()

        if (u_x, u_y) == goal:
            optimal_path = []
            current = (u_x, u_y)
            while current is not None:
                optimal_path.append(current)
                current = path[current]
            optimal_path.reverse()
            return True, optimal_path, move_count

        for j in range(directions):
            v_x = u_x + x_move[j]
            v_y = u_y + y_move[j]

            if (0 <= v_x < N) and (0 <= v_y < N) and graph[v_x][v_y] == 1 and (v_x, v_y) not in visited:
                v = (v_x, v_y)
                queue.append((v, move_count + 1))  
                visited.add(v)
                path[v] = (u_x, u_y)
                print_direction(j, v_x, v_y)

    return False, [], 0

def print_path(optimal_path):
    print("Optimal shortest path:")
    for node in optimal_path:
        print(f"({node[0]}, {node[1]})")

def traverse_2d_plane(graph, source, directions, x_move, y_move, N, goal):
    found, optimal_path, move_count = bfs(graph, source, directions, x_move, y_move, N, goal)

    if found:
        print("Goal found")
        print(f"Total moves needed to reach the goal: {move_count}")
        print_path(optimal_path)
    else:
        print("Goal cannot be reached from the starting block")

def get_matrix_from_user():
    N = int(input("Enter the size of the matrix (N x N): "))
    graph = []
    print("Enter the matrix row by row (each row should have N elements separated by spaces):")
    for _ in range(N):
        row = list(map(int, input().split()))
        graph.append(row)
    return graph, N

def get_coordinates_from_user(prompt):
    print(prompt)
    x = int(input("Enter the x-coordinate: "))
    y = int(input("Enter the y-coordinate: "))
    return (x, y)

def main():
    graph, N = get_matrix_from_user()
    source = get_coordinates_from_user("Enter the coordinates of the source (starting point):")
    goal = get_coordinates_from_user("Enter the coordinates of the goal (destination point):")

    traverse_2d_plane(graph, source, 4, [1, -1, 0, 0], [0, 0, 1, -1], N, goal)

if __name__ == "__main__":
    main()


# 0, 0, 1, 0, 1
# 0, 1, 1, 1, 1
# 0, 1, 0, 0, 1
# 1, 1, 0, 1, 1
# 1, 0, 0, 0, 1

# Enter the size of the matrix (N x N): 5
# Enter the matrix row by row (each row should have N elements separated by spaces):
# 0 0 1 0 1
# 0 1 1 1 1
# 0 1 0 0 1
# 1 1 0 1 1
# 1 0 0 0 1
# Enter the coordinates of the source (starting point):
# Enter the x-coordinate: 0
# Enter the y-coordinate: 2
# Enter the coordinates of the goal (destination point):
# Enter the x-coordinate: 4
# Enter the y-coordinate: 0