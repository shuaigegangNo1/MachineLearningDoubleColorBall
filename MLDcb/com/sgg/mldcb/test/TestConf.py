import configparser

if __name__ == "__main__":
    cf = configparser.ConfigParser()
    cf.read("ConfigParser.conf")

    # 返回所有的section
    s = cf.sections()
    print("section:", s)

    print("*" * 70)
    o1 = cf.options("mysql")
    print("options:mysql", o1)
    o2 = cf.options("个人信息")
    print("options:个人信息", o2)
    o3 = cf.options("add")
    print("options:add", o3)
    o4 = cf.options("del")
    print("options:del", o4)

    print("*" * 70)
    v1 = cf.items("mysql")

    # v1=cf.options("mysql")
    print("items:mysql=", v1)
    for v in v1:
        print("mysql_item", v[1])
    v2 = cf.items("个人信息")
    print("items:个人信息", v2[1][1])
    v3 = cf.items("add")
    print("items:add", v3)
    v4 = cf.items("del")
    print("items:del", v4)
