from board import Board
from ai import AI


class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.turn = "X"

    def run(self):
        print("Connect Four — you are X.")
        while True:
            self.board.print()
            if self.turn == "X":
                try:
                    raw = input("Column (1-7), or q: ").strip().lower()
                except (EOFError, KeyboardInterrupt):
                    print("\nGame exited.")
                    return

                if raw == "q":
                    print("Game quit.")
                    return

                try:
                    col_num = int(raw)
                except ValueError:
                    print("Invalid input. Enter a column number (1-7).")
                    continue

                if not 1 <= col_num <= 7:
                    print("Column out of range. Enter a number between 1 and 7.")
                    continue

                col = col_num - 1
                if self.board.is_column_full(col):
                    print(f"Column {col_num} is full. Choose another column.")
                    continue
            else:
                col = self.ai.choose_column(self.board)
                if col is None:
                    if self.board.full():
                        print("Draw.")
                    else:
                        print("AI has no valid moves.")
                    return

            if self.board.drop(col, self.turn) is None:
                print("Column unavailable.")
                if self.turn == "O":
                    return
                continue

            # Task 2: Consistent game termination
            if self.board.winner(self.turn):
                self.board.print()
                print(self.turn, "wins!")
                return

            if self.board.full():
                self.board.print()
                print("Draw.")
                return

            self.turn = "O" if self.turn == "X" else "X"
