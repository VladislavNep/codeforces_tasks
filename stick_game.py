"""
Играют два игрока.  Есть 10 палочек. Игроки по очереди берут от одной до трёх палочек.
Играют до тех пор пока не закончатся палочки. Тот кто взял последним - тот проиграл.

Реализуйте игру таким образом, чтобы могли играть два человека. Изначально есть 10 палочек.
На каждом ходу выводите на консоль текущее количество оставшихся палочек и просите ввести количество палочек,
которое хочет взять игрок (который делает ход).
"""


def can_take(sticks_taken, remaining_sticks):
    return 1 <= sticks_taken <= 3 and sticks_taken <= remaining_sticks


def switch_player_turn(turn, player_1, player_2):
    return player_1 if turn == player_2 else player_2


def end_of_game(sticks):
    return sticks <= 0


def game():
    player_1 = input("Назови себя игрок 1 \n")
    player_2 = input("Назови себя игрок 2 \n")
    player_turn = player_1
    number_of_sticks = int(input("Сколько палочек для игры хотите? \n"))
    while not end_of_game(number_of_sticks):
        taken = int(input(f"{player_turn} ваш ход. Вы можете взять от 1 до 3 палочек. \n"))

        if not can_take(taken, number_of_sticks):
            print(f"В игре {number_of_sticks} палочек, вы взяли {taken}. \nможно взять только 1, 2, 3 или же вы взяли "
                  f"больше чем осталось палочек. Попробуйте еще \n")
            continue

        number_of_sticks -= taken
        print(f"Палочек было взято: {taken}")

        if end_of_game(number_of_sticks):
            print(f"Палочки закончились. \nИгра окончена, игрок {player_turn} проиграл")
            break

        player_turn = switch_player_turn(player_turn, player_1, player_2)


game()
