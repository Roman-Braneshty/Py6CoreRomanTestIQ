class Roman:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def name(self):
        return f'Hi {self.name}:{self.age}'

    def print_hi(self):
        print(f'Hi, {self.name}')


student = Roman('Vlad', 32)
student.print_hi()

if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
