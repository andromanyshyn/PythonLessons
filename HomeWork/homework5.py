# class Bank:
#
#     def __init__(self, balance=0):
#         self.__balance = balance
#
#     def get_balance(self):
#         print(f"Баланс рахунку - {self.__balance}")
#
#     def set_balance(self, value):
#         if type(value) not in (int, float):
#             raise ValueError("Некоректне значення")
#         self.__balance = value
#
#     def withdraw(self, value):
#         if type(value) not in (int, float):
#             raise ValueError("Некоректне значення")
#         self.__balance -= value
#         if self.__balance < 0:
#             raise ValueError("not enough money")
#
#
#
#
# user1 = Bank()
#
# user1.get_balance()
# user1.set_balance(5000)
# user1.get_balance()
# user1.withdraw(6000)
# user1.get_balance()





import random
class Coin:

    def __init__(self, n, sideup=["heads", "tails"]):
        self.__sideup = sideup
        self.n = n

    def toss(self):
        for i in range(self.n):
            print(random.choice(self.__sideup))


c = Coin(3)
c.toss()