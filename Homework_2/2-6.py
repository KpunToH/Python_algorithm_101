import random


k = input("Добрый день!\n"
      "Сыграем в игру?\n"
      "Вам надо отгадать загаданное комьютером целое число (от 0 до 100) за 10 попыток.\n"
      "Компьютер будет указывать, где находится ваше предположение относительно искомого числа\n"
      "y = играем, n = завершаем работу программы ")
while k != "n":
    if k == "y":
        goal = random.randint(0, 100)
        step = 0
        maxstep = 10

        while step < maxstep:
            user_guess = int(input("Какое число загадал компьютер?"))
            if user_guess > goal:
                print("Ваше число больше искомого!")
            elif user_guess == goal:
                print("Вы победили, поздравляю!")
                break
            else:
                print("Ваше число меньше искомого!")
            step += 1

        if step == maxstep:
            print(f"Загаданное компьютером число было {goal}")
            print("Вы проиграли.Попробуйте еще раз!")

    else:
        print("Команда не распознана, пожалуйста, начните заново")
    k = input("Сыграем еще? y = да, y = нет ")

print("До свидания!")
