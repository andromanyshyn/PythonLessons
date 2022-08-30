# Написати скріпт який приймає від користувача числа та додає їх, закінчити виконання скріпта коли
# сума квадратів прийманих чисел буде більша за 100. В результаті виводить суму всіх чисел.

# suma = 0
# finally_suma = 0
#
# while True:
#     num = int(input())
#     suma = suma + num ** 2
#     finally_suma += num
#     if suma > 100:
#         break
#
# print(finally_suma)


# Написати скріпт який додає до елементів ліста номера, до прикладу
# count = 0
#
# names = ["Serhii", "Ivan"]
# for i in names:
#     count += 1
#     print(str(count) + ")", i)


#
# output:
# 1) Serhii
# 2) Ivan

# suma = 0
#
# while True:
#     num = int(input())
#     suma += num
#     if num == 0:
#         print(suma)
#         break


# while True:
#     num = int(input())
#     if num < 10:
#         continue
#     elif num > 100:
#         break
#     else:
#         print(num)


# Написати програму яка аналізує елементи числовго ліста,
# якщо елемент більший за 10 то виводить його і перевіряє чи це дробове число,
# якщо число дробове то пише про це, в іншому випадку переходить до наступного числа.
# Якщо елемент менший за 10 то виводить елемент, якщо елемент дробовий то пише нам про це.


lst = [25, 10, 3, 22, 112, 11.5, 5.4, 1.5]

for i in lst:
    if i > 10:
        print(i)
        if type(i) == float:
            print(i, "дробове число")
        else:
            continue
    elif i < 10:
        print(i)
        if type(i) == float:
            print(i, "дробове число")

