import random

def guess_the_number():
    hidden_number = random.randint(1, 20)
    attempts = 0

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 20. Попробуйте угадать его.")

    while True:
        try:
            guess = int(input("Введите ваше предположение: "))
            attempts += 1

            if guess < 1 or guess > 20:
                print("Пожалуйста, введите число от 1 до 20.")
            elif guess < hidden_number:
                print("Слишком мало! Попробуйте еще раз.")
            elif guess > hidden_number:
                print("Слишком много! Попробуйте еще раз.")
            else:
                print(f"Поздравляем! Вы угадали число {hidden_number} за {attempts} попыток.")
                break
        except ValueError:
            "У вас неправильное число!"  
guess_the_number()