import os
from tic_tac_toe import TicTacToe

def main():
    game = TicTacToe()
    while True:
        game.print_board()
        while not game.done:
            game.get_player_move()
            game.check_win_or_draw()
            if game.done:
                break
            game.make_move()
            game.check_win_or_draw()
            game.print_board()
        
        try:
            next_game = int(input("\nDigite 1 para sair do jogo ou qualquer outro número para jogar novamente: "))
            if next_game == 1:
                break
            else:
                game.reset()
        except ValueError:
            game.reset()

if __name__ == "__main__":
    main()