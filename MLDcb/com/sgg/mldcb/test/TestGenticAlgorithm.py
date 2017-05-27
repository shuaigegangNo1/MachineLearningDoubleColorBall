import random


def cross_cover(r1, r2):
    i = random.randint(1, len(r1) - 2)
    return r1[0:i] + r2[i:]


if __name__ == "__main__":
    dcb_data = [
        [3, 6, 11, 17, 21, 31, 7, 451.9],
        [1, 3, 7, 18, 23, 27, 12, 384.6],
        [5, 6, 7, 12, 13, 18, 12, 292.0],
        [10, 14, 19, 22, 25, 29, 12, 263.6],
        [2, 12, 16, 19, 27, 30, 11, 262.2],
        [9, 12, 14, 20, 26, 27, 4, 259.1],
        [5, 6, 13, 17, 19, 28, 1, 214.1],
        [5, 6, 13, 18, 23, 31, 11, 181.1],
        [1, 8, 12, 13, 24, 27, 8, 180.4],
        [6, 9, 15, 24, 25, 26, 9, 176.8]]
    # print(dcb_data[0][0])dcb_data[1]
    # print(dcb_data[0][1])
    # print(dcb_data[1])
    # for i in dcb_data[1]:
    #     print(i)
    #     print(len(dcb_data[0]))

    print("cross_cover=", cross_cover(dcb_data[0], dcb_data[1]))
    print("sorted by No_Prize=", sorted(dcb_data, key=lambda x: x[0]))
    # print("sorted by No_Prize=", dcb_data.sort(dcb_data[i][6] for i in range(10)))
