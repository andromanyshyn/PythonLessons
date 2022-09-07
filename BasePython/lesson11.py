# def say_hello():
#     print("Hello")
#
#
# say_hello()


# def say_hi():
#     print("Hi")
#
#
# def name():
#     print("Andrew")
#
#
# def main():
#     name()
#     say_hi()
#
#
# main()


# def name(user):
#     print(f"Hello, {user}")
#
#
# name("andrew")
# name("Sergii")
# name("Oleg")
# name("Vika")


# def suma(*kwargs):
#     count = 0
#     for i in kwargs:
#         count += i
#     print(count)
#
#
# def double(x):
#     return x * 2
#
#
# print(double(10))


# Написати функцію яка перевіряє чи користувач вводить реальний вік,
# умова перевірки: вік має бути більший за 0 та менший за 120.
# Якщо перевірка успішна функція виводить <userName> - <age> років! Інакше повертає False.


# def age_check(age, user):
#     if 0 < age < 120:
#         print(f"{user} - {age}, років!")
#     else:
#         return False
#
#
# age_check(35, "Andrew")