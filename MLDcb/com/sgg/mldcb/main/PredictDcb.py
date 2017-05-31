from MLDcb.com.sgg.mldcb.util.MysqlUtil import MysqlUtil
from MLDcb.com.sgg.mldcb.algorithm.ThirdNeutralNetworks import ThirdNeutralNetworks
import numpy as np
from MLDcb.com.sgg.mldcb.util.FormatUtil import FormatUtil
from MLDcb.com.sgg.mldcb.util.ConfUtil import get_mysql_parameters


def predict_dcb_wining(row):
    fu = FormatUtil()
    x = fu.tuple_to_list(row)

    X = np.array([[0, 0, 0, 1, 1, 1, 0],
                  [0, 0, 0, 0, 0, 1, 1],
                  [0, 0, 1, 1, 1, 1, 1],
                  [0, 0, 0, 1, 1, 1, 0],
                  [0, 0, 1, 1, 1, 1, 0],
                  [0, 0, 0, 0, 1, 1, 1],
                  [0, 0, 0, 0, 1, 1, 1],
                  [0, 0, 0, 0, 0, 1, 1]])
    y = np.array([[1],
                  [1],
                  [1],
                  [1],
                  [0],
                  [0],
                  [0],
                  [0]])
    tnn = ThirdNeutralNetworks(X, y)
    return tnn.predict(np.array(x))


if __name__ == "__main__":
    # acquire mysql connecting parameters
    ip, user, pwd, database, table, conn = get_mysql_parameters()
    # connect database
    mysqlUtil = MysqlUtil(ip, user, pwd, database, table, conn)
    mysqlUtil.mysql_connect()
    row = mysqlUtil.mysql_query_one()
    print("-----row-----", row)
    print("-----row[1:8]------", row[1:8])
    predict_dcb_wining(row)
    # fu = FormatUtil()
    # x = fu.tuple_to_list(row)
    #
    # X = np.array([[0, 0, 0, 1, 1, 1, 0],
    #               [0, 0, 0, 0, 0, 1, 1],
    #               [0, 0, 1, 1, 1, 1, 1],
    #               [0, 0, 0, 1, 1, 1, 0],
    #               [0, 0, 1, 1, 1, 1, 0],
    #               [0, 0, 0, 0, 1, 1, 1],
    #               [0, 0, 0, 0, 1, 1, 1],
    #               [0, 0, 0, 0, 0, 1, 1]])
    # y = np.array([[1],
    #               [1],
    #               [1],
    #               [1],
    #               [0],
    #               [0],
    #               [0],
    #               [0]])
    # tnn = ThirdNeutralNetworks(X, y)
    # tnn.predict(np.array(x))
