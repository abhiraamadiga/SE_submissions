import random


class AI:
    def choose_column(self, board, me="O", opponent="X"):
        num_cols = len(board.grid[0]) if board.grid else 7
        num_rows = len(board.grid) if board.grid else 6
        legal = [c for c in range(num_cols) if board.grid[0][c] == "."]
        if not legal:
            return None

        # 1. Take immediate winning move if one exists
        for col in legal:
            for r in range(num_rows - 1, -1, -1):
                if board.grid[r][col] == ".":
                    board.grid[r][col] = me
                    if board.winner(me):
                        board.grid[r][col] = "."
                        return col
                    board.grid[r][col] = "."
                    break

        # 2. Block immediate opponent winning move if one exists
        for col in legal:
            for r in range(num_rows - 1, -1, -1):
                if board.grid[r][col] == ".":
                    board.grid[r][col] = opponent
                    if board.winner(opponent):
                        board.grid[r][col] = "."
                        return col
                    board.grid[r][col] = "."
                    break

        # 3. Prefer center and adjacent columns, falling back to any legal move
        preferred_order = [3, 2, 4, 1, 5, 0, 6]
        for col in preferred_order:
            if col in legal:
                return col

        return random.choice(legal)
