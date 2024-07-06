class TicTacToe:

    def __init__(self):
        self._board = [' ' for _ in range(9)]

    def display_board(self):
        for row in [self._board[counter * 3: (counter + 1) * 3] for counter in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def assign_marker(self, position, marker):
        self._board[position - 1] = marker

    def available_positions(self):
        return [index + 1 for index, value in enumerate(self._board) if value == ' ']

    def is_winner(self, position, marker):
        # Row Check
        row_index = (position - 1) // 3
        row = self._board[row_index * 3: (row_index + 1) * 3]
        if all([spot == marker for spot in row]):
            return True

        # Column check
        column_index = (position - 1) % 3
        column = [self._board[column_index + i * 3] for i in range(3)]
        if all([spot == marker for spot in column]):
            return True

        # Diagonals Check
        if (position - 1) % 2 == 0:
            diagonal1 = [self._board[spot] for spot in [0, 4, 8]]
            if all((spot == marker) for spot in diagonal1):
                return True

            diagonal2 = [self._board[spot] for spot in [2, 4, 6]]
            if all((spot == marker) for spot in diagonal2):
                return True

        return False

    def replay(self):
        retry = None
        while not (retry == 'Y' or retry == 'N'):
            retry = input('\nDo you want to play again? Y or N: ').upper()

        if retry == 'Y':
            self._board = [' ' for _ in range(9)]
            return True
        else:
            return False

    @staticmethod
    def display_positions():
        def generate_row(row_index):
            return [str(i + 1) for i in range(row_index * 3, (row_index + 1) * 3)]

        for row in [generate_row(row_index) for row_index in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
