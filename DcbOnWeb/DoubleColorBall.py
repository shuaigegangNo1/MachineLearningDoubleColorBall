from flask import Flask, render_template, request
import sqlite3 as sql
from DcbOnWeb.MysqlUtil import MysqlUtil

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add_double_color_ball', methods=['POST', 'GET'])
def add_double_color_ball():
    if request.method == 'POST':
        # try:
        r1 = request.form['r1']
        r2 = request.form['r2']
        r3 = request.form['r3']
        r4 = request.form['r4']
        r5 = request.form['r5']
        r6 = request.form['r6']
        b7 = request.form['b7']
        dcb_id = request.form['id']
        data_time = '2017-04-13'
        total_sales = 0
        no_first_prize = 0
        no_second_prize = 0

        ip = "localhost"
        user = "root"
        pwd = ""
        database = "double_color_ball"
        # database = "testcsv"
        table = "dcb"
        conn = ""

        mysqlUtil = MysqlUtil(ip, user, pwd, database, table, conn)
        mysqlUtil.mysql_connect()
        mysqlUtil.mysql_insert(dcb_id, r1, r2, r3, r4, r5, r6, b7, data_time, total_sales, no_first_prize,
                               no_second_prize)
        #     with sql.connect("database.db") as con:
        #         cur = con.cursor()
        #
        #         cur.execute("INSERT INTO dcb (r1,r2,r3,r4,r5,r6,b7) "
        #                     "VALUES(?, ?, ?, ?,?,?,?)", (r1, r2, r3, r4, r5, r6, b7))
        #
        #         con.commit()
        #         msg = "Record successfully added"
        # except:
        #     con.rollback()
        #     msg = "error in insert operation"
        #
        # finally:
        #     return render_template("result.html", msg=msg)
        #     con.close()
        msg = "Record successfully added"
        return render_template("result.html", msg=msg)


@app.route('/echarts')
def charts():
    # return render_template('testEcharts.html')
    return render_template('testZxt.html')


if __name__ == '__main__':
    # app.run()
    ip = "localhost"
    user = "root"
    pwd = ""
    database = "double_color_ball"
    # database = "testcsv"
    table = "dcb"
    conn = ""

    mysqlUtil = MysqlUtil(ip, user, pwd, database, table, conn)
    mysqlUtil.mysql_connect()
    # mysqlUtil.mysql_insert('88888', '1', '2', '3', '4', '5', '6', '7', '"2017-04-13"', '0', '0', '0')
    # sql="select * from dcb order by id desc limit 0,5;"
    # sql="select * from dcb order by id desc limit "+str(0)+","+str(5)
    rows = mysqlUtil.mysql_query(0, 7)
    print([row[0] for row in rows])
    print([row[2] for row in rows])
    # print(rows[1][2])
    # for row in rows:
    #     print (row[2])

    # print(rows)
