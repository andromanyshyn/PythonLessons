def some_func(file):
    with open(file, "w", encoding="utf-8") as f:
        f.write("Любе речення")


some_func("test_file.txt")


def read_file(file):
    with open(file, "r", encoding= "utf-8") as f:
        tekst = f.read()

    return tekst


print(read_file("test_file.txt"))
