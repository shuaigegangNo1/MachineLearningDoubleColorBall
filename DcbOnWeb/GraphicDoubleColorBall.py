# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, request
import json
from MLDcb.com.sgg.mldcb.util.MysqlUtil import MysqlUtil
from MLDcb.com.sgg.mldcb.util import ConfUtil
from MLDcb.com.sgg.mldcb.main.PredictDcb import predict_dcb_wining

app = Flask(__name__)


def get_dcb_data(data):
    ip, user, pwd, database, table, conn = ConfUtil.get_mysql_parameters()
    mysql_util = MysqlUtil(ip, user, pwd, database, table, conn)
    mysql_util.mysql_connect()
    rows = mysql_util.mysql_query(data["num"], 7)
    mysql_util.mysql_close()
    return rows


@app.route('/')
def index():
    return render_template('doubleColorBallShow.html')


'''
receive data from frontend, transform it into Json data
configure database and query from database
process data locally, then return it to frontend
'''


@app.route('/postDcbData', methods=['POST'])
def post_double_color_ball_data():
    data = json.loads(request.get_data())
    rows = get_dcb_data(data)
    data["location"] = [1, 2, 3, 4, 5, 6, 7]
    dcb_fields = ["red1", "red2", "red3", "red4", "red5", "red6", "b1"]
    for i in range(0, dcb_fields.__len__()):
        data.__setitem__(dcb_fields[i], [row[i + 1] for row in rows])
    data["num"] = int(data["num"]) + 7
    return jsonify(data)


@app.route('/predictLottery', methods=['POST'])
def predict_lottery():
    data = json.loads(request.get_data())
    group = data["group"]
    rows = get_dcb_data(data)
    result = predict_dcb_wining(rows[group])
    data["result"] = result
    return jsonify(data)


if __name__ == '__main__':
    app.run()
