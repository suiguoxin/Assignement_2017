from fractions import gcd


# function to calculate the least common multiple
def lcm(list):
    lcm = 1
    for i in list:
        lcm = lcm * i / gcd(lcm, i)
    return lcm


# initiate LH Algorithm
def init(A, B):
    Lx = []
    Ly = []
    for i in range(m):
        Lx.append(i + 1)
    for i in range(n):
        Ly.append(m + i + 1)
    print '********* initialisation ***********'
    print 'Lx :', Lx
    print 'Ly :', Ly

    P = [[] for _ in range(n)]
    Q = [[] for _ in range(m)]
    for i in range(n):
        for j in range(m + n + 1):
            if j < m:
                P[i].append(B[j][i])
            elif j == m + i:
                P[i].append(1)
            elif j == m + n:
                P[i].append(1)
            else:
                P[i].append(0)
    print('P :'), P

    for i in range(m):
        for j in range(m + n + 1):
            if j == m + n:
                Q[i].append(1)
            elif j >= m:
                Q[i].append(A[i][j - m])
            elif j == i:
                Q[i].append(1)
            else:
                Q[i].append(0)
    print('Q :'), Q

    return Lx, Ly, P, Q


def singularize(P, su, s):
    muls = []
    for i in range(len(P)):
        mul = s / P[i][su]
        muls.append(mul)
        for j in range(len(P[0])):
            P[i][j] = int(P[i][j] * mul)
    return muls


def regularize(P, su, muls):
    mi = 0
    mm = 999999
    for i in range(len(P)):
        if abs(P[i][m + n]) < mm:
            mi = i
            mm = abs(P[i][m + n])
    for i in range(len(P)):
        if i != mi:
            mul = P[i][su] / P[mi][su]
            for j in range(m + n + 1):
                P[i][j] = P[i][j] -   mul * P[mi][j]
        else:
            for j in range(m + n + 1):
                P[i][j] /= muls[i]
    return


def calculate_lx(P):
    Lx = []
    for i in range(m + n):
        flag = 0
        for j in range(len(P)):
            if P[j][i] != 0:
                if flag == 0:
                    flag = 1
                else:
                    Lx.append(int(i + 1))
                    break
    return Lx


# calculate x, y with Lx, Ly and print the result
def transform(Lx, Ly):
    x = [0] * m
    y = [0] * n
    for idx, val in enumerate(Lx):
        if val > m:
            y[val - m - 1] = 1
    for idx, val in enumerate(Ly):
        if val <= m:
            x[val - 1] = 1

    print '********* result ***********'
    print('Lx:'), Lx
    print('Ly:'), Ly
    print 'x :', x
    print 'y :', y

    return


# re-calculate su
def finish_condition(Lx, Ly):
    su = m + n
    L = [0] * su
    for i in Lx:
        L[i - 1] = 1
    for i in Ly:
        if L[i - 1] == 1:
            su = i - 1
    return su


def lemke_howson(A, B):
    Lx, Ly, P, Q = init(A, B)

    su = 0
    fl = 0  # operation in P or in Q
    print '********* iteration ***********'
    while su != m + n:
        if fl == 0:
            s = lcm([row[su] for row in P])
            s = abs(s)

            muls = singularize(P, su, s)
            regularize(P, su, muls)

            Lx = calculate_lx(P)
            print ('Lx:'), Lx

            su = finish_condition(Lx, Ly)
            fl = 1
        elif fl == 1:
            s = lcm([row[su] for row in Q])
            s = abs(s)

            muls = singularize(Q, su, s)
            regularize(Q, su, muls)
            print('Q :'), Q

            Ly = calculate_lx(Q)
            print ('Ly:'), Ly

            su = finish_condition(Lx, Ly)
            fl = 0

    transform(Lx, Ly)


#A = [[4, 3], [1, 2]]
#B = [[2, 1], [3, 4]]

#A = [[12, 8, 6], [8, 12, 8]]
#B = [[5, 5, 8], [1, 8, 4]]

A = [[3, 2], [1, 3]]
B = [[1, 5], [4, 2]]

m = len(A)
n = len(A[0])

lemke_howson(A, B)
