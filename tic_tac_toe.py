import random
from utils import clear_screen

class TicTacToe:
    PLAYER_X = "X"
    PLAYER_O = "O"
    EMPTY = " "

    def __init__(self):
        self.reset()

    def print_board(self):
        clear_screen()
        board_str = "\n"
        board_str += "   0   1   2\n"
        for i, row in enumerate(self.board):
            board_str += f"{i}  " + " | ".join(row) + " \n"
            board_str += "  -----------\n"
        print(board_str.rstrip("  -----------\n"))

    def reset(self):
        self.board = [[self.EMPTY for _ in range(3)] for _ in range(3)]
        self.done = ""

    def check_win_or_draw(self):
        lines = [
            self.board[0], self.board[1], self.board[2],
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
            # Diagonal
            [self.board[0][2], self.board[1][1], self.board[2][0]],
            [self.board[0][0], self.board[1][1], self.board[2][2]]
        ]

        for player in [self.PLAYER_X, self.PLAYER_O]:
            if any(line == [self.PLAYER_X, self.PLAYER_X, self.PLAYER_X] for line in lines):
                self.done = self.PLAYER_X.lower()
                clear_screen()
                self.print_board()
                print(f"\n{self.PLAYER_X} venceu!")
                return

            if any(line == [self.PLAYER_O, self.PLAYER_O, self.PLAYER_O] for line in lines):
                self.done = self.PLAYER_O.lower()
                clear_screen()
                self.print_board()
                print(f"\n{self.PLAYER_O} venceu!")
                return

        if all(cell != self.EMPTY for row in self.board for cell in row):
            self.done = "d"
            clear_screen()
            self.print_board()
            print("\nEmpate!")
            return

    def get_player_move(self):
        while True:
            try:
                x = int(input("Digite a linha do seu próximo lance (0-2): "))
                y = int(input("Digite a coluna do seu próximo lance (0-2): "))

                if x not in range(3) or y not in range(3):
                    print("Coordenadas inválidas. Tente novamente.")
                    continue

                if self.board[x][y] != self.EMPTY:
                    print("Posição já preenchida. Tente novamente.")
                    continue

                self.board[x][y] = self.PLAYER_X
                break
            except ValueError:
                print("Entrada inválida. Digite um número entre 0 e 2.")

    def make_move(self):
        available_moves = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == self.EMPTY]
        if available_moves:
            x, y = random.choice(available_moves)
            self.board[x][y] = self.PLAYER_O