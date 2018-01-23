import sqlite3


con = sqlite3.connect("../abcd.db")

# 유니코드 인코딩 문제가 발생할 경우 주석을 해제하고 실행을 하라는데...
# con.text_factory = str

# 메모리 DB를 사용할때
# con = sqlite3.connect(":memory:")

print(type(con))
print(dir(con))

# Cursor 객체 생성 이후로 진행 ㄱㄱ
cur = con.cursor()
print(type(cur))
print(dir(cur))

table_scheme = '''
CREATE TABLE tbl_abcd (
  title VARCHAR (100),
  text VARCHAR (1000),
  img_url VARCHAR (100),
  posted_date VARCHAR (100)
)
'''
cur.execute(table_scheme)
con.commit()

result = cur.execute("SELECT * FROM sqlite_master")
for table in result.fetchall():
    print(table)

# 자원 회수
con.close()