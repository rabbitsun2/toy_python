import pymysql # pymysql 임포트

def create_hi(name):

    print(f'Hi, {name}')

    # 전역변수 선언부
    conn = None
    cur = None

    sql = ""

    # 메인 코드
    conn = pymysql.connect(host='127.0.0.1', user='hr',
                       password='123456', db='hr', charset='utf8') # 접속정보

    cur = conn.cursor() # 커서생성

    sql = "CREATE TABLE IF NOT EXISTS userTable(id char(4), userName char(10), email char(15), birthYear int)"

    cur.execute(sql)

    conn.commit()
    conn.close()

def insert_hi(name):

    conn = None
    cur = None


    data1 = ""
    data2 = ""
    data3 = ""
    data4 = ""

    sql = ""


    # 메인 코드
    conn = pymysql.connect(host='127.0.0.1', user='hr', password='123456', db='hr', charset='utf8')
    cur = conn.cursor()

    while(True):
        data1 = input("사용자 ID를 입력하세요(엔터 클릭시 종료): ")     # data1변수에 ID 입력받기

        if data1 == "":
            break;


        data2 = input("사용자 이름을 입력하세요: ")
        data3 = input("사용자 이메일을 입력하세요: ")
        data4 = input("사용자 출생연도를 입력하세요: ")

        sql = "INSERT INTO userTable VALUES('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
        cur.execute(sql)    # 커서로 sql 실행
        
    conn.commit()   # 최종 저장
    conn.close()    # 접속 종료
        
        
    


if __name__ == '__main__':
    # create_hi('PyCharm')
    insert_hi('PyCharm')
