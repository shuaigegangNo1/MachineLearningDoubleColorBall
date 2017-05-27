import pymysql


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

    def mysql_query(self):
        try:
            sql = "select * from " + self.table + " limit 10"
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            # print(rows)
        except:
            print(sql + "query failed")
        return rows

    def mysql_query(self, sql):
        try:
            # sql = "select * from " + self.table + " limit 10"
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            # print(rows)
        except:
            print(sql + "query failed")
        return rows

    def mysql_query_one(self):
        try:
            sql = "select * from " + self.table + " order by rand()"
            self.cursor.execute(sql)
            rows = self.cursor.fetchone()
            # print(rows)
        except:
            print(sql + "query failed")
        return rows

    def mysql_insert(self, arg0, arg1, arg2):
        try:
            # sql = "insert into " + self.table + "  values(" +arg0+","+arg1+","+arg2+")"
            sql = "INSERT INTO " + self.table + " VALUES(" + arg0 + "," + arg1 + "," + "'" + arg2 + "'" + ")"

            self.cursor.execute(sql)
            self.conn.commit()
            print(sql + "insert succeed")
        except:
            self.conn.commit()
            print(sql + "insert failed")

    def mysql_close(self):
        self.cursor.close()
        self.conn.close()
