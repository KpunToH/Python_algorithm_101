print("Программа для определения позиции буквы в алфавите.\n"
      "Версия для русского и английского языка  ")
first_letter = ord(input("Введите первую интересующую букву алфавита, пожалуйста "))
second_letter = ord(input("Введите вторую интересующую букву алфавита, пожалуйста "))

if first_letter >= 97 and first_letter <= 122 and second_letter >= 97 and second_letter <= 122:
    print("Позиция первой буквы ", (first_letter - 96))
    print("Позиция второй буквы ", (second_letter - 96))
    print("Расстояние между буквами", (abs(second_letter-first_letter)))
elif first_letter >= 1072 and first_letter <= 1103 and second_letter >= 1072 and second_letter <= 1103:
    print("Позиция первой буквы ", (first_letter - 1071))
    print("Позиция второй буквы ", (second_letter - 1071))
    print("Расстояние между буквами", (abs(second_letter - first_letter)))
else:
    print("Возникла непредвиденная ошибка. \n"
          "Возможно вы ввели неправильный символ, либо взяли буквы из разных алфавитов.Попробуйте еще раз!")
