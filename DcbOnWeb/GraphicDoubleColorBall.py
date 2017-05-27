# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, request
import json
from DcbOnWeb.MysqlUtil import MysqlUtil
from MLDcb.com.sgg.mldcb.util import ConfUtil
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('doubleColorBallShow.html')


@app.route('/postDcbData', methods=['POST'])
def post_double_color_ball_data():
    #  接收前端发来的数据,转化为Json格式
    data = json.loads(request.get_data())
    # configure database
    ip, user, pwd, database, table, conn = ConfUtil.get_mysql_parameters()
    mysql_util = MysqlUtil(ip, user, pwd, database, table, conn)
    mysql_util.mysql_connect()
    rows = mysql_util.mysql_query(data["num"], 7)
    #  然后在本地对数据进行处理,再返回给前端
    # process data locally, then return it to frontend
    data["location"] = [1, 2, 3, 4, 5, 6, 7]
    dcbs = ["red1", "red2", "red3", "red4", "red5", "red6", "b1"]
    for i in range(0, dcbs.__len__()):
        data.__setitem__(dcbs[i], [row[i + 1] for row in rows])
    data["num"] = int(data["num"]) + 7
    return jsonify(data)


if __name__ == '__main__':
    app.run()
