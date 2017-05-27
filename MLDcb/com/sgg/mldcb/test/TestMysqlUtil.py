from com.sgg.mldcb.util.MysqlUtil import MysqlUtil

if __name__ == "__main__":
    # 打开数据库连接
    ip = "localhost"
    user = "root"
    pwd = ""
    database = "double_color_ball"
    # database = "testcsv"
    table = "dcb"
    conn = ""
    mysqlUtil = MysqlUtil(ip, user, pwd, database, table, conn)
    # mysqlUtil.__init__(ip, user, pwd, database, table)
    sql = "select floor(r1/16) as r1,floor(r2/16) as r2,floor(r3/16) as r3," \
          "floor(r4/16) as r4,floor(r5/16) as r5,floor(r6/16) as r6 ,floor(b1/8) as b1," \
          " noFirstPrize+noSecondPrize*0.3 as point from dcb order by point desc limit 10;"
    mysqlUtil.mysql_connect()
    rows = mysqlUtil.mysql_query(sql)
    dcb_len = len(rows[0])
    # dcb = [[]] * len(rows)
    dcb=[]
    print("dcb", dcb)
    print("len rows[0]", len(rows[0]))
    print("len dcb", len(dcb))
    print("rows=", rows)
    for row in rows:
        # for i in range(len(rows)):
            # dcb[i]=row
            dcb.append(row)
            # # dcb[i].append(row)
            # for j in range(len(dcb)):
            #     # dcb[i][j].append(row[j])
            #     dcb[i][j]=row[j]
    print("dcb[0][7] of type=", type(dcb[0][7]))
    print("dcb[0] len", len(dcb[0]))
    print("sorted by No_Prize=", sorted(dcb, key=lambda x: x[7]))
    rows1 = mysqlUtil.mysql_query_one()
    print("rows1", rows1)
    print(rows1[0])
    print(rows1[1])
    print(rows1[8])
    # mysqlUtil.mysql_insert('9', '666', 'huangWen')
    mysqlUtil.mysql_close()
