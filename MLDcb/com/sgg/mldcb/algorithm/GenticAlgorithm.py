import random
from MLDcb.com.sgg.mldcb.util.MysqlUtil import MysqlUtil

# class GenticAlgorithm(object):
def cross_cover(r1, r2):
    i = random.randint(1, len(r1) - 2)
    return r1[0:i] + r2[i:]


# 随机变异
def mutate(vec):
    domain = [(0, 33), (0, 33), (0, 33), (0, 33), (0, 33), (0, 33), (0, 16)]
    step = 1
    i = random.randint(0, len(domain) - 1)
    print("i", i)
    if random.random() < 0.5 and vec[i] > domain[i][0]:
        print("enter first branch")
        return vec[0:i] + [vec[i] - step] + vec[i + 1:]
    elif vec[i] < domain[i][1]:
        print("enter second branch")
        return vec[0:i] + [vec[i] + step] + vec[i + 1:]


if __name__ == "__main__":
    vec = [6, 9, 2, 7, 8, 6, 6]
    # mutate(vec)
    print(mutate(vec))

    # g = GenticAlgorithm()
    # g.mutate()
    # print("random", random.random())
    # 打开数据库连接
    ip = "localhost"
    user = "root"
    pwd = ""
    database = "double_color_ball"
    # database = "testcsv"
    table = "dcb"
    conn = ""
    mysqlUtil = MysqlUtil(ip, user, pwd, database, table, conn)
    mysqlUtil.mysql_connect()
    rows=mysqlUtil.mysql_query_one()
    print("rows",rows)
    print("rows[1:8] of type",type(rows[1:8]))
    row_dcb=[]
    for row in rows[1:8]:
        row_dcb.append(row)
        print(row)
    # print("query",mysqlUtil.mysql_query_one())
    print(mutate(row_dcb))
    mysqlUtil.mysql_close()