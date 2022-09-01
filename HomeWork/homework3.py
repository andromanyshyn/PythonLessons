# 1 )

# lst = []
# while True:
#     num = int(input("Введіть цифру: "))
#     lst.append(num)
#     if len(lst) == 10:
#         break
# print("Цикл завершено ! ")


# 2)

# lst = [1, 15, 13, 2, 0, 11]
# while True:
#     num = int(input("Введіть елемент зі списку : "))
#     lst.remove(num)
#     if len(lst) < 1:
#         break
# print("Цикл завершено : ", lst)
#
#
# 3)

# lst = []
# while True:
#     num = int(input("Введіть цифру: "))
#     if num == 0:
#         break
#     lst.append(num)
#     print("індекс елементу - ", lst.index(num))
# print("Цикл завершено !")


# import random
#
#
# def generator():
#     counter = 0
#     random_list = []
#     while counter <= 10:
#         random_list.append(random.randint(0, 100))
#         counter += 1
#
#     return random_list
#
#
# random_list = generator()
# print(random_list)

# while True:
#     a = int(input())
#     if a not in random_list:
#         print("Такого елементу немає в лісті")
#     elif a in random_list:
#         print(random_list.index(a))
#     elif a == 0:
#         break


# a = [1, 2, 3, 1, 3, 4, 1]
# num = int(input())
# for i in a:
#     if i == num:
#         a.remove(i)
#
# print(a)
