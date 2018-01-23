import sqlite3
import csv


def get_db_con() -> sqlite3:
    return sqlite3.connect("../abcd.db")


def print_all():
    # Read
    with get_db_con() as db:
        cur = db.cursor()

        sql_select = "SELECT * FROM 'tbl_abcd'"

        cur.execute(sql_select)
        results = cur.fetchall()
        for idx, value in enumerate(results):
            print('%d. %s' % (idx, value))


# Create
with get_db_con() as db:
    cur = db.cursor()

    # one
    sql_insert = "INSERT INTO 'tbl_abcd' VALUES ('제목', '내용', '이미지 주소', '등록일')"
    cur.execute(sql_insert)

    # many
    sql_insert_many = "INSERT INTO 'tbl_abcd' ('img_url', 'posted_date', 'text', 'title') VALUES (?, ?, ?, ?)"
    # img_url,posted_date,text,title

    csv_file = open("../result.csv")
    reader = csv.reader(csv_file)
    item_list = list(reader)
    item_list = item_list[1:]

    cur.executemany(sql_insert_many, item_list)

print_all()


# Read
print("*" * 50)
print("Read")
with get_db_con() as db:
    cur = db.cursor()

    sql_select = "SELECT * FROM tbl_abcd WHERE title LIKE :keyword OR text LIKE :keyword"
    param = {"keyword": "%" + "abcd" + "%"}
    result = cur.execute(sql_select, param)

    row_list = result.fetchall()
    for idx, value in enumerate(row_list):
        print('%d. %s' % (idx, value))

'''
# Update
print("*" * 50)
print("Update")
with get_db_con() as db:
    cur = db.cursor()

    sql_update = "UPDATE 'tbl_abcd' SET 'text' = 'ABCD짱짱!! 파이썬 재밌어요'"
    cur.execute(sql_update)

print_all()


# Delete
print("*" * 50)
print("Delete")
with get_db_con() as db:
    cur = db.cursor()

    sql_delete = "DELETE FROM 'tbl_abcd'"
    cur.execute(sql_delete)

print_all()
'''