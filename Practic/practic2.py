from math import sqrt, pi



print(sqrt(4))

a = int(input("Мінімальне число здорового сну: "))
b = int(input("Максимальне число здорового сну : "))
h = int(input("Години сну зараз: "))

if h > b:
    print("Пересип")
elif h < a:
    print("Недосип")
elif a < h <= b:
    print("Це нормально")
else:
    print("Choose correct option")


a = int(input("Число a: "))
b = int(input("Число b: "))
c = int(input("Число c: "))

p = (a + b + c) / 2

s = sqrt(p * (p - a) * (p - b) * (p - c))
print(s)


figure = input("Введіть назву фігури: ")

if figure == "Прямокутник":
    a = float(input())
    b = float(input())
    print(a * b)
elif figure == "Трикутник":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print(s)
elif figure == "Круг":
    r = float(input())
    s = pi * (r ** 2)
    print(s)


x = int(input())

if -15 < x <= 12 or 14 < x < 17 or x >= 19:
    print(True)
else:
    print(False)


