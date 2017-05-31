from flask import Flask, render_template, request
from MLDcb.com.sgg.mldcb.util.MysqlUtil import MysqlUtil
from MLDcb.com.sgg.mldcb.util import ConfUtil

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


'''
1.receive data from frontend
2.prepare inserted data
3.configure database and insert data
'''


@app.route('/add_double_color_ball', methods=['POST', 'GET'])
def add_double_color_ball():
    if request.method == 'POST':
        form_params = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'b7']
        r1, r2, r3, r4, r5, r6, b7 = [request.form[param] for param in form_params]
        dcb_id = request.form['id']
        data_time = '2017-04-13'
        total_sales = 0
        no_first_prize = 0
        no_second_prize = 0

        ip, user, pwd, database, table, conn = ConfUtil.get_mysql_parameters()
        mysql_util = MysqlUtil(ip, user, pwd, database, table, conn)
        mysql_util.mysql_connect()
        insert_data = [dcb_id, r1, r2, r3, r4, r5, r6, b7, data_time, total_sales, no_first_prize, no_second_prize]
        mysql_util.mysql_insert(insert_data)
        mysql_util.mysql_close()

        msg = "Record successfully added"
        return render_template("result.html", msg=msg)


@app.route('/echarts')
def charts():
    return render_template('lineChart.html')


if __name__ == '__main__':
    app.run()
