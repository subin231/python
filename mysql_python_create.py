# sql 사용하기 위한 라이브러리 포함문
import pymysql as sql
# cursor에 담아 사용하기위한 라이브러리 포함문
import pymysql.cursors
# data를 정렬하여 index와 함께 같이 보기위한 table 구조도형식의 라이브러리 포함문
import pandas as pd

#DB연결 정리 자기자리의 데이터만 가져올 수 있다.
#이후에 데이터 원격 커넥션 활용방법 확인 필요함.
conn = sql.connect(host='127.0.0.1', user='root', password='1234',db='college', charset='utf8',
                   autocommit=True, cursorclass=pymysql.cursors.DictCursor)

# 연결 확인 절차
if(conn):
    print("connection 성공")
else:
    print("connection 실패")

#DB 생성문
sqlDB = '''
create database soloDB 
    '''
#Create Table 생성문
sqlCT =\
'''
create table userTable(
id          int primary key auto_increment,
userName    varchar(20) not null,
email       varchar(100) not null,
birthday    int not null)
'''

#데이터 insert 문
sqlIN = '''
insert into usertable (id ,userName ,email ,birthday) values
(1,'홍지윤','hong@naver.com',1996);
'''


# 생성 결과 담는 곳
#cur변수에 conn.cursor 담기
cur = conn.cursor()

#  2024-07-10 조건 추가 필요
# 조건에 맞는 sql식으로 변경 필요함 DB Create, Table Create, Insert문까지 정리 필요함.
cur.execute(sqlIN)

print("데이터가 정상적으로 추가되었습니다.")

#index를 나타내기위해 detchall메소드 사용
result = cur.fetchall()

#연결해제
conn.close()

#데이터 show
print(result)
