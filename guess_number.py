"""
Задание:
    Отгадай число
"""
import random
def get_user_guess():
    """
    Запрашивает у пользователя число
     и проверяет его на корректность ввода.
     В случае некорректного ввода (если введено не число),
     пользователю выводится сообщение об ошибке.
    """
    try:
        guess = int(input("Угадайте загаданное число"))
    except TypeError as te:
        print("Не корректый ввод",te)
    play_game(guess)
    return guess

def play_game(guess):
    """
    Основная логика игры,
    управляющая процессом угадывания числа,
    включая генерацию случайного числа,
    обработку попыток пользователя и предложение о новой игре после угадывания.
    """
    mysterious_number = random.randint(0,100)
    attempts = 0
    while True:
        attempts += 1
        if guess < mysterious_number:
            guess = int(input("Не угадал \n Подсказка: загадонное число больше\n"))
        elif guess > mysterious_number:
            guess = int(input("Не угадал \n Подсказка: загадонное число меньше\n"))
        elif guess == mysterious_number:
            print ("Поздравляю ты угадал!!! \n Загадонное число:", \
                    guess, "\nЧисло попыток:", attempts)
            break
if __name__ == "__main__":
    get_user_guess()
