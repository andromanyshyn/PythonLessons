# Написати пайтон скріпт який приймає імена з ліста, аналізує
# скільки букв в імені є, якщо кількість букв більша
# за 4 виводить ім'я та каже, що ім'я реальне в іншому випадку переходить на інше ім'я.


lst = ["Oleg", "vika", "Vitalik", "Valera", "Ola"]

for i in lst:
    if len(i) > 4:
        print(i, "- Це ім'я реальне")
    else:
        continue

