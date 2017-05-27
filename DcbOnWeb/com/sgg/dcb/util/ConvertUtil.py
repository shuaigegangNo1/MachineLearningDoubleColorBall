def convert_int_to_str(num):
    return "'" + str(num) + "'"


if __name__ == "__main__":
    a = 4
    b = convert_int_to_str(4)
    print(b)
