import os
import json


class Users:

    def __init__(self):
        self.username = None
        self.password = None
        self.id = None

    def registration(self, username, password, id):
        self.username = username
        self.password = password
        self.id = id
        d = {"username": username, "password": password, "id": id}
        print((json.dumps(d)))
        if not os.path.exists("database.json"):
            with open("database.json", "w") as database:
                database.write(json.dumps(d))
        else:
            print("Файл Існує")



user = Users()
user.registration("Moriss", "1234", "1")



