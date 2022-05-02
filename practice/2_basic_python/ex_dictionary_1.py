# 딕셔너리 예제
# 정도윤(Doyun Jung)

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    grade = {'pey': 10, 'julliet': 99 }
    print(grade['julliet'])

    a = {1:'a', 2:'b'}
    print(a[1])
    print(a[2])

    a = {'a':1, 'b':2}
    print(a['a'])
    print(a['b'])

    dic = {'name': 'pey', 'phone': '01199333323', 'birth': '1970'}
    print(dic['name'])
    print(dic['phone'])
    print(dic['birth'])

    print(dic.keys())
    print(dic.values())

    # 딕셔너리
    for k in dic.keys() :
        print(k)

    # 딕셔너리 삭제
    del dic['name']

    # 딕셔너리 값
    for k in dic.values():
        print(k)

    # 딕셔너리 추가
    dic['name'] = 'pey'

    # 딕셔너리 쌍 자료형
    for k in dic.items():
        print(k)

    print(dic.get('nokey'))

    print(dic.get('fo', 'bar'))

    print( 'name' in dic )
    print( 'email' in dic )
