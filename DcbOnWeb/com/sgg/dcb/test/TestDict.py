if __name__ == "__main__":
    # dcb = {"red1": 1, "red2": 2}
    # print(dcb)
    # # dcb.setdefault("red3",44)
    # dcb.__setitem__("red4", 666)
    # for (k, v) in dcb.items():
    #     print("dcb[%s]" % k, v)
    # print()
    dcb = {}
    dcbs = ["red1", "red2", "red3", "red4", "red5", "red6", "b1"]
    for i in range(0, 7):
        dcb.__setitem__(dcbs[i],i)
        print(dcbs[i])
        #     dcb.__setitem__(d, i)
    print(dcb)
