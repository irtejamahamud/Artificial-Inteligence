import random

def print_direction(m, x, y):
    directions = ["Down", "Up", "Right", "Left"]
    print(f"Moving {directions[m]} ({x}, {y})")

def st_dfs(graph, u, directions, x_move, y_move, N, goal):
    graph[u[0]][u[1]] = 0
    for j in range(directions):
        v_x = u[0] + x_move[j]
        v_y = u[1] + y_move[j]
        if (0 <= v_x < N) and (0 <= v_y < N) and graph[v_x][v_y] != 0:
            v_depth = u[2] + 1
            print_direction(j, v_x, v_y)
            if (v_x, v_y) == goal:
                return True, v_depth

            graph[v_x][v_y] = 0
            found, depth = st_dfs(graph, (v_x, v_y, v_depth), directions, x_move, y_move, N, goal)
            if found:
                return True, depth
    return False, 0

def generate_grid(N, obstacles):
    grid = [[1] * N for _ in range(N)]
    for _ in range(obstacles):
        while True:
            x = random.randint(0, N - 1)
            y = random.randint(0, N - 1)
            if grid[x][y] != 0:
                grid[x][y] = 0
                break
    return grid

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def get_coordinates(N):
    while True:
        try:
            x, y = map(int, input(f"Enter the coordinates (x y) within the {N}x{N} grid: ").split())
            if not (0 <= x < N and 0 <= y < N):
                raise ValueError("Coordinates out of range.")
            return x, y
        except ValueError as e:
            print("Invalid input. Please enter valid coordinates.")

def main():
    N = int(input("Enter the size of the grid (N x N): "))
    obstacles = int(input("Enter the number of obstacles: "))
    grid = generate_grid(N, obstacles)
    print("Generated Grid:")
    print_grid(grid)
    
    source_x, source_y = get_coordinates(N)
    goal_x, goal_y = get_coordinates(N)
    
    source = (source_x, source_y, 0)
    goal = (goal_x, goal_y)

    found, depth = st_dfs(grid, source, 4, [1, -1, 0, 0], [0, 0, 1, -1], N, goal)

    if found:
        print("Goal found")
        print("Number of moves required =", depth)
    else:
        print("Goal cannot be reached from the starting block")

if __name__ == "__main__":
    main()
5
