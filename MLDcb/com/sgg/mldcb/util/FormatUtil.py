import numpy as np
import math
from MLDcb.com.sgg.mldcb.util.ConstUtil import const


class FormatUtil(object):
    def tuple_to_list(self, row):
        a = np.array(row[const.one:const.eight]) / const.seventeen
        print(a)
        x = [] * const.seven
        for i in range(len(a)):
            x.append(math.floor(a[i]))
        print(x)
        return x

    def convert_int_to_str(self, num):
        return "'" + str(num) + "'"


if __name__ == "__main__":
    print(const.company)
