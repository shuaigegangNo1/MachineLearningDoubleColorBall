import pymysql

from DcbOnWeb.com.sgg.dcb.util.ConvertUtil import convert_int_to_str


class MysqlUtil(object):
    def __init__(self, host, user, password, database, table, conn):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.table = table
        self.conn = conn

    def mysql_connect(self):
        try:
            self.conn = pymysql.connect(self.host, self.user, self.password, self.database)
            self.cursor = self.conn.cursor()
            print("connect mysql succeed")
        except:
            print("connect mysql failed.")

    def mysql_query(self, start, length):
        try:
            sql = "select * from " + self.table + " limit " + str(start) + "," + str(length)
            print(sql)
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
        except:
            print(sql + "query failed")
        return rows

    # def mysql_query(self, sql):
    #     try:
    #         # sql = "select * from " + self.table + " limit 10"
    #         self.cursor.execute(sql)
    #         rows = self.cursor.fetchall()
    #         # print(rows)
    #     except:
    #         print(sql + "query failed")
    #     return rows

    def mysql_query_one(self):
        try:
            sql = "select * from " + self.table + " order by rand()"
            self.cursor.execute(sql)
            rows = self.cursor.fetchone()
            # print(rows)
        except:
            print(sql + "query failed")
        return rows

    def mysql_insert(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11):
        try:
            # sql = "insert into " + self.table + "  values(" +arg0+","+arg1+","+arg2+")"
            # sql = "INSERT INTO " + self.table + " VALUES(" + arg0 + "," + arg1 + "," + arg2 + "," \
            #       + arg3 + "," + arg4 + "," + arg5 + "," + arg6 + ")"
            arg0 = convert_int_to_str(arg0)
            arg1 = convert_int_to_str(arg1)
            arg2 = convert_int_to_str(arg2)
            arg3 = convert_int_to_str(arg3)
            arg4 = convert_int_to_str(arg4)
            arg5 = convert_int_to_str(arg5)
            arg6 = convert_int_to_str(arg6)
            arg7 = convert_int_to_str(arg7)
            arg8 = convert_int_to_str(arg8)
            arg9 = convert_int_to_str(arg9)
            arg10 = convert_int_to_str(arg10)
            arg11 = convert_int_to_str(arg11)

            sql = "INSERT INTO " + self.table + " VALUES(" + arg0 + "," + arg1 + "," + arg2 + "," \
                  + arg3 + "," + arg4 + "," + arg5 + "," + arg6 + "," + arg7 + "," + arg8 + "," + arg9 + "," + arg10 + "," + arg11 + ")"
            print("sql", sql)

            self.cursor.execute(sql)
            self.conn.commit()
            print(sql + "insert succeed")
        except:
            self.conn.commit()
            print(sql + "insert failed")

    def mysql_close(self):
        self.cursor.close()
        self.conn.close()
