from tictactoe import TicTacToe
from player import Player


def play():
    print('Welcome to Tic Tac Toe\n')
    TicTacToe.display_positions()

    game = TicTacToe()

    play_game = True

    while play_game:
        player1_marker = None
        while not (player1_marker == 'X' or player1_marker == 'O'):
            player1_marker = input('\nPlayer 1: Choose a marker X or O: ').upper()

        player2_marker = 'O' if player1_marker == 'X' else 'X'

        player1 = Player(player1_marker, 'Player 1')
        player2 = Player(player2_marker, 'Player 2')

        print(f'\nPlayer 1 marker: {player1_marker.upper()}.\nPlayer 2 marker: {player2_marker.upper()}')

        gameon = True
        turn = player1_marker

        while gameon:
            def make_move(player):
                spot = player.choose_spot(game.available_positions())
                game.assign_marker(spot, player.marker)
                game.display_board()

                if game.is_winner(spot, player.marker):
                    print(f'\nCongratulations {player.name}, You won the game!')
                    return False

                elif len(game.available_positions()) == 0:
                    print('\nIt is a Draw')
                    return False

                return True

            if turn == player1_marker:
                gameon = make_move(player1)
                turn = player2_marker
                if not gameon:
                    break

            if turn == player2_marker:
                gameon = make_move(player2)
                turn = player1_marker

        play_game = game.replay()


if __name__ == '__main__':
    play()
