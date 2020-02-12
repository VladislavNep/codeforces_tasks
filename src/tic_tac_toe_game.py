"""
Вы попробуете реализовать игру в крестики-нолики размером 3х3.
Сделайте метод, который выводит на каждом ходу текущее положение с линейками, крестиками и ноликами.
Также вам понадобится реализовать способ проверки наличия выигрышной комбинации. Договоримся,
что клетки поля будут пронумерованы от 0 до 8 и пользователи будут вводить индекс поля,
чтобы поставить там крестик или нолик.
"""

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8)]


def print_state(state):
    for i, v in enumerate(state):
        if (i + 1) % 3 == 0:
            print(f'{v}')
        else:
            print(f'{v}|', end='')


def get_winner(state, combinations):
    for (x, y, z) in combinations:
        if state[x] == state[y] and state[y] == state[z] and (state[x] == 'X' or state[x] == '0'):
            return state[x]

    return ''


def correct_input(index, board):
    board_index = (i for i in range(0, 9))
    return index in board_index and board[index] == ' '


def switch_correct_input(current_sing):
    return 'X' if current_sing == '0' else '0'


def play_game(board):
    current_sing = 'X'
    while (get_winner(board, winning_combinations) == '') and (' ' in board):

        index = int(input(f'Где хочешь нарисовать {current_sing}? \n'))

        if not correct_input(index, board):
            print("Вы можете использовать только пустые клетки и индыксы от 0 до 8. Попробуйте еще...")
            continue

        board[index] = current_sing
        print_state(board)

        winner_sing = get_winner(board, winning_combinations)
        if winner_sing != '':
            print(f"У нас есть победитель {winner_sing}")

        current_sing = switch_correct_input(current_sing)


play_game(board)
