# n_queens.py

class NQueensProblem:
    def __init__(self, n):
        self.n = n

    def initial_state(self):
        return ()

    def is_goal(self, state):
        return len(state) == self.n

    def get_actions(self, state):
        col = len(state)
        if col >= self.n: return []
        return [row for row in range(self.n) if self.is_safe(state, col, row)]

    def result(self, state, row):
        return state + (row,)

    def is_safe(self, state, col, row):
        for c, r in enumerate(state):
            if r == row or abs(r - row) == abs(c - col):
                return False
        return True

    def count_remaining_legal_moves(self, state):
        """support for advanced heuristic"""
        total_safe = 0
        current_col = len(state)
        for col in range(current_col, self.n):
            safe_in_col = 0
            for row in range(self.n):
                if self.is_safe(state, col, row):
                    safe_in_col += 1
            if safe_in_col == 0: return -1 
            total_safe += safe_in_col
        return total_safe
