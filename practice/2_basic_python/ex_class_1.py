
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('hello')

    cal1 = Calculator()
    cal2 = Calculator()

    print(cal1.add(3))
    print(cal1.add(4))

    print(cal2.add(3))
    print(cal2.add(7))
