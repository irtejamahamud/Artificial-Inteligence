class NQueen:
    def __init__(self, N):
        self.N = N
        self.solutions = []

    def print_solution(self, board):
        for row in board:
            print(" ".join(map(str, row)))
        print()

    def is_safe(self, board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        for i, j in zip(range(row, self.N, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def solve_nq_util(self, board, col):
        if col >= self.N:
            solution = []
            for i in range(self.N):
                solution.append(list(board[i]))
            self.solutions.append(solution)
            return True

        res = False
        for i in range(self.N):
            if self.is_safe(board, i, col):
                board[i][col] = 1
                res = self.solve_nq_util(board, col + 1) or res
                board[i][col] = 0  # BACKTRACK

        return res

    def solve_nq(self):
        board = [[0] * self.N for _ in range(self.N)]
        if not self.solve_nq_util(board, 0):
            print(f"No solution exists for {self.N} queens")
            return False
        print(f"Number of distinct solutions for {self.N} queens:", len(self.solutions))
        for solution in self.solutions:
            self.print_solution(solution)
        return True


if __name__ == "__main__":
    n = int(input("Number of queens to place: "))
    queen = NQueen(n)
    queen.solve_nq()
