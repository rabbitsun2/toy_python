import pymysql # pymysql 임포트

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




