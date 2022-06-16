class Roman:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def name(self):
        return f'Hi {self.name}:{self.age}'


def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
