import random


def cross_cover(r1, r2):
    i = random.randint(1, len(r1) - 2)
    return r1[0:i] + r2[i:]


# mutate randomly
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

