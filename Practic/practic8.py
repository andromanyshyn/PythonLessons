from string import digits
from string import ascii_letters


class Registration:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @staticmethod
    def check_password_dictionary(password):
        password = password + "\n"
        with open("C:/users/Andrew/PycharmProjects/HomeWork/easy_passwords.txt") as file:
            if password in file:
                return True
            else:
                return False

    @staticmethod
    def is_include_only_latin(password):
        for i in ascii_letters:
            if i in password:
                return True
        return False

    @staticmethod
    def is_include_all_register(password):
        for i in ascii_letters:
            if i in password:
                return True
        return False

    @staticmethod
    def is_include_digit(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @property
    def password(self):
        return self.__pasword

    @password.setter
    def password(self, value):
        if type(value) is not str:
            raise TypeError("Пароль должен быть строкой")
        if len(value) < 5 or len(value) > 11:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_digit(value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_all_register(value):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if not Registration.is_include_only_latin(value):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if Registration.check_password_dictionary(value) is True:
            raise ValueError('Ваш пароль содержится в списке самых легких')
        self.__pasword = value

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        if type(value) is not str:
            raise TypeError("Wrong data type")
        if value.count("@") == 0 or value.count("@") > 1:
            raise ValueError("Логин должен содержать один символ '@'")
        if value.count(".") == 0:
            raise ValueError("Логин должен содержать символ '.'")
        if value.index(".") < value.index("@"):
            raise ValueError
        self.__login = value


r1 = Registration('qwerty@rambler.ru', 'QwrRt124') # здесь хороший логин
print(r1.login, r1.password)  # qwerty@rambler.ru QwrRt124

