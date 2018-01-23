from flask import Flask
from flask import request
import json
import sqlite3


def get_db_con() -> sqlite3:
    return sqlite3.connect("../abcd.db")


app = Flask(__name__)
app.debug = True


@app.route("/list", methods=['GET', 'POST'])
def list_all():
    with get_db_con() as con:
        cur = con.cursor()

        sql = "SELECT * FROM tbl_abcd"
        result = cur.execute(sql)
        row_list = result.fetchall()

        json_data = []

        for idx, row in enumerate(row_list):
            print("{} {}".format(idx, row))
            json_data.append({
                "title": row[0],
                "text": row[1],
                "img_url": row[2],
                "posted_date": row[3]
            })

    return json.dumps(json_data, ensure_ascii=False).encode("UTF-8")


@app.route("/search", methods=['GET'])
def search():
    q = request.args.get("q")
    print("q-"+q)

    with get_db_con() as con:
        cur = con.cursor()

        sql_select = "SELECT * FROM tbl_abcd WHERE title LIKE :keyword OR text LIKE :keyword"
        param = {"keyword": "%" + q + "%"}
        result = cur.execute(sql_select, param)
        row_list = result.fetchall()

        json_data = []

        for idx, row in enumerate(row_list):
            print("{} {}".format(idx, row))
            json_data.append({
                "title": row[0],
                "text": row[1],
                "img_url": row[2],
                "posted_date": row[3]
            })

    return json.dumps(json_data, ensure_ascii=False).encode("UTF-8")


@app.route("/add", methods=['POST'])
def delete():
    param_json = request.get_json()
    param = (param_json["title"], param_json["text"])
    print(param)

    with get_db_con() as db:
        cur = db.cursor()

        sql_insert = "INSERT INTO 'tbl_abcd' ('title', 'text') VALUES (?, ?)"
        cur.execute(sql_insert, param)

    return json.dumps({"result":"OK"}, ensure_ascii=False).encode("UTF-8")


@app.route("/remove", methods=['DELETE'])
def remove_all():
    with get_db_con() as db:
        cur = db.cursor()

        sql_delete = "DELETE FROM 'tbl_abcd'"
        cur.execute(sql_delete)

    return json.dumps({"result": "OK"}, ensure_ascii=False).encode("UTF-8")


if __name__ == "__main__":
    app.run()