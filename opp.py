import random

def guess_the_number():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Ваш вариант: "))
        attempts += 1

        if guess < secret_number:
            print("Больше. Попробуйте еще раз.")
        elif guess > secret_number:
            print("Меньше. Попробуйте еще раз.")
        else:
            print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.")
            break

if __name__ == "__main__":
    guess_the_number()
