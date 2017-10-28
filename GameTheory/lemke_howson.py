from fractions import gcd


# function to calculate the least common multiple
def lcm(list):
    lcm = 1
    for i in list:
        lcm = lcm * i / gcd(lcm, i)
    return lcm


# initiate LH Algorithm
def init(A, B, m, n):
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
    for i in range(len(P)):
        a = P[i][su]
        if a != 0:
            for j in range(len(P[0])):
                P[i][j] = int(P[i][j] * s / abs(a))
    return P


def regularize(P, su, s):
    mi = 0
    mm = 9999
    for i in range(len(P)):
        if P[i][m + n] < mm:
            mi = i
            mm = P[i][m + n]
    for i in range(len(P)):
        if i != mi:
            for j in range(m + n + 1):
                P[i][j] = P[i][j] - P[mi][j]
        else:
            times = s / B[su][i]
            for j in range(m + n + 1):
                P[i][j] /= times
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
        if val <= m:
            y[idx] = 1
    for idx, val in enumerate(Ly):
        if val <= m:
            x[idx] = 1

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
    Lx, Ly, P, Q = init(A, B, m, n)

    su = 0
    fl = 0  # operation in P or in Q
    print '********* iteration ***********'
    while su != m + n:
        if fl == 0:
            s = lcm([row[su] for row in P])
            s = abs(s)

            singularize(P, su, s)
            regularize(P, su, s)

            Lx = calculate_lx(P)
            print ('Lx:'), Lx

            su = finish_condition(Lx, Ly)
            fl = 1
        elif fl == 1:
            s = lcm([row[su] for row in Q])
            s = abs(s)

            singularize(Q, su, s)
            regularize(Q, su, s)
            print('Q :'), Q

            Ly = calculate_lx(Q)
            print ('Ly:'), Ly

            su = finish_condition(Lx, Ly)
            fl = 0

    transform(Lx, Ly)


# A = [[4, 3], [1, 2]]
# B = [[2, 1], [3, 4]]

A = [[12, 8, 6], [8, 12, 8]]
B = [[5, 5, 8], [1, 8, 4]]

m = len(A)
n = len(A[0])
lemke_howson(A, B)
