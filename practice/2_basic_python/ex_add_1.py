# This is a sample Python script.

result = 0

def print_hi(name):
    print(f'Hi, {name}')  # 

    a = [1, 2, 3]
    print(a[0] + a[2])

def add(num):
    global result
    result += num

    return result


if __name__ == '__main__':
    print_hi('PyCharm')
    print(add(3))
    print(add(4))