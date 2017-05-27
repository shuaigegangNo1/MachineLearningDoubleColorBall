#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import math
import time

# 四种优化算法
# 接受一个变量定义域的列表和针对每一组变量的成本函数
# 返回最低成本以及该成本对应的变量组(最优解)

# 随机搜索算法
# 随机产生若干个变量组,找到最小的成本
def randomoptimization(domain, costf):
    best = 999999999
    bestr = None
    for i in range(1000):
        r = [random.randint(domain[i][0], domain[i][1]) for i in range(len(domain))]
        cost = costf(r)
        if cost < best:
            best = cost
            bestr = r
    return (best, bestr)


# 爬山法
# 根据一组随机解在附近找到最优解,可以确保局部最优,但不能保证全局最优
# 理论上比随机算法复杂,效果应该好,但实际上不如随机算法,单纯的爬山法应用很少
def hillclimb(domain, costf):
    sol = [random.randint(domain[i][0], domain[i][1]) for i in range(len(domain))]  # 产生随机解

    while 1:
        neighbors = []
        # 产生若干附近的解
        for j in range(len(domain)):
            if sol[j] > domain[j][0]:
                neighbors.append(sol[0:j] + [sol[j] - 1] + sol[j + 1:])
            if sol[j] < domain[j][1]:
                neighbors.append(sol[0:j] + [sol[j] + 1] + sol[j + 1:])

        current = costf(sol)
        best = current
        # 从附近的解中找到成本最小的解
        for j in range(len(neighbors)):
            cost = costf(neighbors[j])
            if best > cost:
                best = cost
                sol = neighbors[j]
        # 如果附近的解中成本最小的和原来的成本相同,说明到达局部最优,算法终止
        if best == current:
            break
        return best, sol


# 模拟退火算法
# 爬山法的推广,爬山法只选择更优的解,而退火算法不总是会接受一个更优的解,而且还会在退火的开始阶段表现接受较差的解
# 随着退火过程的不断进行,算法越来越不可能接受较差的解,直到最后它将只接受更优的解
# 效果比爬山算法好,但比随机算法没好太多,并且偶尔表现比随机算法还差
def annealingoptimize(domain, costf, T=10000.0, cool=0.95, step=1):
    vec = [random.randint(domain[i][0], domain[i][1]) for i in range(len(domain))]

    while T > 0.1:  # 只要温度大于0.1度,就继续退火
        i = random.randint(0, len(domain) - 1)
        dir = random.randint(-step, step)
        vecb = vec[:]
        vecb[i] += dir  # 随机邻近的解
        if vecb[i] < domain[i][0]:
            vecb[i] = domain[i][0]
        elif vecb[i] > domain[i][1]:
            vecb[i] = domain[i][1]

        ea = costf(vec)
        eb = costf(vecb)
        # 开始阶段表现有可能接受较差的解,但可能性逐渐降低,直到最后只接受更优的解
        if (eb < ea or random.random() < pow(math.e, -(eb - ea) / T)):
            vec = vecb
        T = T * cool  # 温度降低
    return costf(vec), vec


# 遗传算法
# 在随机的一群解中找到最优的一部分解,淘汰其他解,然后在最优的部分解中进行杂交和变异,产生更优的解,多次迭代,最后返回最优解
# 结合了上述算法的优点和改进了它们的缺点
# 随机种群的选择结合了随机搜索算法的广泛性和随机性,克服了爬山和退火的初始随机解选择的局限性和片面性
# 杂交变异和优胜劣汰结合了爬山和退火的选择更优和优秀算法总是局部相邻,克服了随机算法的完全随机
# 整体表现不俗,缺点是执行时间较长
def geneticoptimize(domain, costf, popsize=50, step=1, mutprob=0.2, elite=0.2, maxiter=100):
    # 随机变异
    def mutate(vec):
        i = random.randint(0, len(domain) - 1)
        if random.random() < 0.5 and vec[i] > domain[i][0]:
            return vec[0:i] + [vec[i] - step] + vec[i + 1:]
        elif vec[i] < domain[i][1]:
            return vec[0:i] + [vec[i] + step] + vec[i + 1:]

    # 优秀杂交
    def crossover(r1, r2):
        i = random.randint(1, len(domain) - 2)
        return r1[0:i] + r2[i:]

    pop = []
    # 生成随机种群
    for i in range(popsize):
        vec = [random.randint(domain[i][0], domain[i][1]) for i in range(len(domain))]
        print("vec=",vec)
        pop.append(vec)

    toplite = int(elite * popsize)
    scores = None
    for i in range(maxiter):  # 迭代进化
        scores = [(costf(v), v) for v in pop]
        scores.sort()
        ranked = [v for (s, v) in scores]
        pop = ranked[0:toplite]  # 优胜劣汰

        # 种群繁殖
        while (len(pop) < popsize):
            if random.random() < mutprob:
                c = random.randint(0, toplite)
                pop.append(mutate(ranked[c]))  # 变异
            else:
                c1 = random.randint(0, toplite)
                c2 = random.randint(0, toplite)
                pop.append(crossover(ranked[c1], ranked[c2]))  # 杂交
            #        print(scores[0][0])
    return scores[0][0], scores[0][1]  # 返回最优


if __name__ == "__main__":
    # 人的信息：名字+出发地
    people = [
        ('Seymour', 'BOS'),
        ('Franny', 'DAL'),
        ('Zooey', 'CAK'),
        ('Walt', 'MIA'),
        ('Buddy', 'ORD'),
        ('Les', 'OMA')
    ]
    destination = 'LGA'  # 目的地
    flights = {}

    # 读入航班信息
    with open('../../../../resources/schedule.txt') as f:
        for line in f:
            # 出发地、目的地、起飞时间、到达时间、机票价格
            origin, dest, depart, arrive, price = line.split(',')
            flights.setdefault((origin, dest), [])
            flights[(origin, dest)].append((depart, arrive, int(price)))


    # 航班时间转化为分钟
    def getminutes(t):
        x = time.strptime(t, '%H:%M')
        return x[3] * 60 + x[4]


    # 打印方案：r存储的是从第一个人到最后一个人的往返航班号序列
    def printschedule(r):
        for d in range(len(r) // 2):
            name = people[d][0]
            origin = people[d][1]
            out = flights[(origin, destination)][r[2 * d]]
            ret = flights[(destination, origin)][r[2 * d + 1]]
            print('%10s%10s %5s-%5s $%3s %5s-%5s $%3s' % (name, origin, out[0], out[1], out[2], ret[0], ret[1], ret[2]))


    # 成本函数
    def schedulecost(sol):
        if sol is None:
            return 999999999
        totalprice = 0
        latestarrival = 0
        earliestdep = 24 * 60

        for d in range(len(sol) // 2):
            origin = people[d][1]
            outbound = flights[(origin, destination)][int(sol[2 * d])]
            returnf = flights[(destination, origin)][int(sol[2 * d + 1])]

            # 机票成本
            totalprice += outbound[2]
            totalprice += returnf[2]
            # 统计“往”最迟的到达时间
            if latestarrival < getminutes(outbound[1]):
                latestarrival = getminutes(outbound[1])
            # 统计“返”最早的出发时间
            if earliestdep > getminutes(returnf[0]):
                earliestdep = getminutes(returnf[0])

        totalwait = 0
        for d in range(len(sol) // 2):
            origin = people[d][1]
            outbound = flights[(origin, destination)][int(sol[2 * d])]
            returnf = flights[(destination, origin)][int(sol[2 * d + 1])]
            # 等待时间成本
            totalwait += latestarrival - getminutes(outbound[1])
            totalwait += getminutes(returnf[0]) - earliestdep

        # 是否需要过夜的住宿成本
        if latestarrival > earliestdep:
            totalprice += 50
        return totalprice + totalwait



    domain=[(0,9)]*(2*len(people))
    print("domain",domain)
    print("schedulecost",schedulecost)
    (best,bestr)=randomoptimization(domain,schedulecost)
    print(best)
    printschedule(bestr)

    (best1,bestr1)=hillclimb(domain,schedulecost)
    print(best1)
    printschedule(bestr1)

    (best2,bestr2)=annealingoptimize(domain,schedulecost)
    print(best2)
    printschedule(bestr2)

    (best3,bestr3)=geneticoptimize(domain,schedulecost)
    print(best3)
    printschedule(bestr3)
    vec_data = [5, 9, 5, 6, 7, 0, 4, 6, 4, 1, 2, 6]
    for i in range(len(vec_data)//2):
        print(vec_data[2*i])
        print(vec_data[2 * i+1])
    print("cost=",schedulecost(vec_data))