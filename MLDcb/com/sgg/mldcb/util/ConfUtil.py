import configparser
from MLDcb.com.sgg.mldcb.util.ConstUtil import const


def get_mysql_parameters():
    cf = configparser.ConfigParser()
    cf.read(const.project_path + "/MLDcb/resources/ConfigParser.conf")
    ip = cf.get("mysql", "db_host")
    user = cf.get("mysql", "db_user")
    pwd = cf.get("mysql", "db_password")
    database = cf.get("mysql", "db_database")
    table = cf.get("mysql", "db_table")
    conn = cf.get("mysql", "db_conn")
    return ip, user, pwd, database, table, conn
