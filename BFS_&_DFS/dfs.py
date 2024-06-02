def print_direction(m, x, y):
    if m == 0:
        print("Moving Down ({}, {})".format(x, y))
    elif m == 1:
        print("Moving Up ({}, {})".format(x, y))
    elif m == 2:
        print("Moving Right ({}, {})".format(x, y))
    else:
        print("Moving Left ({}, {})".format(x, y))

def st_dfs(graph, u, directions, x_move, y_move, N, goal):
    graph[u[0]][u[1]] = 0
    for j in range(directions):
        v_x = u[0] + x_move[j]
        v_y = u[1] + y_move[j]
        if (0 <= v_x < N) and (0 <= v_y < N) and graph[v_x][v_y] == 1:
            v_depth = u[2] + 1
            print_direction(j, v_x, v_y)
            if v_x == goal[0] and v_y == goal[1]:
                return True, v_depth

            graph[v_x][v_y] = 0
            found, depth = st_dfs(graph, (v_x, v_y, v_depth), directions, x_move, y_move, N, goal)
            if found:
                return True, depth
    return False, 0

def init():
    graph = [
        [0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 0, 0, 1]
    ]
    N = len(graph)
    print(N)
    source_x = 0
    source_y = 2
    goal_x = 4
    goal_y = 0
    source = (source_x, source_y, 0)
    goal = (goal_x, goal_y, 999999)

    found, depth = st_dfs(graph, source, 4, [1, -1, 0, 0], [0, 0, 1, -1], N, goal)

    if found:
        print("Goal found")
        print("Number of moves required =", depth)
    else:
        print("Goal cannot be reached from the starting block")

init()