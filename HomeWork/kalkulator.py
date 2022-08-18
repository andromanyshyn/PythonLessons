# Написати простий каркулятор для двох чесел (a i b). З наступними математичними операціями:
# +, -, *, /, pow. Числа а і b - приймаються від користувача.
# Відповідь при діленні і множенні має заокруглюватися до двох чисел після коми.


a = float(input("write down number a : "))
b = float(input("write down number b : "))
option = input("write down option : + - * / pow  ")

if option == "+":
    print(a + b)
elif option == "-":
    print(a + b)
elif option == "*":
    print(round(a + b))
elif option == "/":
    print(round(a + b))
elif option == "pow":
    print(a ** b)
else:
    print("choose the correct option")


