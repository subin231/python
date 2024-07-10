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

#조건 select 문
sqltest = '''
select stdno, stdname, lecno, lecname, regmidscore, regfinalscore, regtotalscore, concat(reggrade,'등급')
  from student a
  join register b
    on a.stdno = b.regstdno
  join lecture c
    on b.reglecno = c.lecno
 order by regtotalscore desc;
    '''

# 조건 결과 담는 곳
#cur변수에 conn.cursor 담기
cur = conn.cursor()
cur.execute(sqltest)

#index를 나타내기위해 detchall메소드 사용
result = cur.fetchall()

#pandas를 이용하여 데이터프레임으로 정렬
df = pd.DataFrame(result)

#연결해제
conn.close()

#데이터 show
print(df)
print(df.count("rows"),"데이터가 조회되었습니다.")