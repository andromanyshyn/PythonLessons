# 4) Написати бота, який виводить число яке ввів користувач
# з консолі, до того моменту поки користувач не введе
# стоп, якщо число = 14, то не виводить його а перекидає на нову ітерацію.


while True:
    number = input("Write down number : ")

    if number == "stop":
        break
    elif number == "14":
        print("Try again")
        continue
    elif number:
        print(number)
    else:
        print("Error !")


print("Цикл завершено !")







