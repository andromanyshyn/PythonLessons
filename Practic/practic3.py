# 1) Є ліст елементів (Назви автомобілів) - прогнати його циклом while та циклом for.

# nameCars = ["Honda", "Citroen", "Bmw", "Mazda", "Mercedes"]

# for i in nameCars:
#     print(i)

# counter = 0
# while counter < len(nameCars):
#     print(nameCars[counter])
#     counter += 1


# 2) Приймати назви авто від користувача поки користувач не введе stop

# while True:
#     nameCars = input("Write down car name: ")
#     if nameCars == "stop":
#         break

# 3) Приймати числа від користувача поки їх сума не буде рівна 100.
# suma = 0
# while True:
#     numbers = int(input())
#     if suma != 100:
#         suma += numbers
#     else:
#         break
# print(suma)

suma = 0
while suma != 100:
    numbers = int(input())
    suma += numbers
print(suma)