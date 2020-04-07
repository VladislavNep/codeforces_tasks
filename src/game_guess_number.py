from random import randint


def game():
    print("я загадал число от 1 до 50 и у тебя есть 6 попыток что бы его отгадать")
    guess_num = randint(1, 50)
    attempt = 0
    while attempt != 6:
        num = int(input())
        attempt += 1

        if num == guess_num:
            return f"Ура! Вы отгадали число {guess_num}"

        elif num > guess_num:
            print(f"Число {num} больше загаданного, попробуйте еще)")

        elif num < guess_num:
            print(f"Число {num} меньше загаданного, попробуйте еще)")

    else:
        return "Ты проиграл, так как не отгадал число за 6 попыток"


print(game())