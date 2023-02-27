mas = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 'S', 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


end = [7, 6]


def posstart():
    for i in mas:
        for j in i:
            if j == 'S':
                fullmas = mas.index(i)
                return [fullmas, mas[fullmas].index(j)]


# def posend():
#     for i in mas:
#         for j in i:
#             if j == 'E':
#                 fullmas = mas.index(i)
#                 return [fullmas, mas[fullmas].index(j)]


m = []
mstart =[]
for i in range(len(mas)):
    m.append([])
    mstart.append([])
    for j in range(len(mas[i])):
        m[-1].append(0)
        mstart[-1].append(0)
pos = posstart()
mstart[pos[0]][pos[1]] = 1
m[pos[0]][pos[1]] = 1


def refresh_m():

    global m

    m = [[] for i in range(len(m))]
    for i in range(len(mstart)):
        for j in mstart[i]:
            m[i].append(j)

flagcheck = False
flagcount = 1


def make_step(k: int, mas: list) -> None:

    global flagcheck
    global flagcount
    global m


    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == k:
                try:
                    if i > 0 and j < len(m[i]) - 1 and m[i - 1][j + 1] == 0 and mas[i - 1][j + 1] == 0:  # верх-право
                        m[i - 1][j + 1] = k + 1
                except IndexError:
                    pass
                try:
                    if i > 0 and j > 0 and m[i - 1][j - 1] == 0 and mas[i - 1][j - 1] == 0:  # верх-лево
                        m[i - 1][j - 1] = k + 1
                except IndexError:
                    pass
                try:
                    if i < len(m) - 1 and j < len(m[i]) and m[i + 1][j + 1] == 0 and mas[i + 1][j + 1] == 0:  # низ-прв
                        m[i + 1][j + 1] = k + 1
                except IndexError:
                    pass
                try:
                    if i < len(m) - 1 and j > 0 and m[i + 1][j - 1] == 0 and mas[i + 1][j - 1] == 0:  # низ-лево
                        m[i + 1][j - 1] = k + 1
                except IndexError:
                    pass
                if i > 0 and m[i - 1][j] == 0 and mas[i - 1][j] == 0:
                    m[i - 1][j] = k + 1
                if j > 0 and m[i][j - 1] == 0 and mas[i][j - 1] == 0:
                    m[i][j - 1] = k + 1
                if i < len(m) - 1 and m[i + 1][j] == 0 and mas[i + 1][j] == 0:
                    m[i + 1][j] = k + 1
                if j < len(m[i]) - 1 and m[i][j + 1] == 0 and mas[i][j + 1] == 0:
                    m[i][j + 1] = k + 1
                flagcheck = True
    if flagcheck:
        flagcount += 1


allpath = {}

def cycle(k, mas) -> None:

    global flagcheck
    global flagcount

    flagcount = 1
    while m[end[0]][end[1]] == 0 and flagcount == k + 1:
        k += 1
        make_step(k, mas)
        flagcheck = False


cycle(0, mas)


def get_path(a = 0) -> None:

    global m

    i, j = end[0], end[1]
    k = m[i][j]
    the_path = [(i, j)]
    flagmove = True

    while k > 1:

        if 0 <= i - 1 <= 9 and 0 <= j + 1 <= 9:
            if i > 0 and j < len(m[i]) - 1 and m[i - 1][j + 1] == k - 1 and flagmove:
                flagmove = False
                i, j = i - 1, j + 1
                the_path.append((i, j))
                k -= 1
        if 0 <= i - 1 <= 9 and 0 <= j - 1 <= 9:
            if i > 0 and j > 0 and m[i - 1][j - 1] == k - 1 and flagmove:
                flagmove = False
                i, j = i - 1, j - 1
                the_path.append((i, j))
                k -= 1
        if 0 <= i + 1 <= 9 and 0 <= j + 1 <= 9:
            if i < len(m) - 1 and j < len(m[i]) and m[i + 1][j + 1] == k - 1 and flagmove:
                flagmove = False
                i, j = i + 1, j + 1
                the_path.append((i, j))
                k -= 1
        if 0 <= i + 1 <= 9 and 0 <= j - 1 <= 9:
            if i < len(m) - 1 and j > 0 and m[i + 1][j - 1] == k - 1 and flagmove:
                flagmove = False
                i, j = i + 1, j - 1
                the_path.append((i, j))
                k -= 1

        if 0 <= i - 1 <= 9 and 0 <= j <= 9:
            if i > 0 and m[i - 1][j] == k - 1 and flagmove:
                flagmove = False
                i, j = i - 1, j
                the_path.append((i, j))
                k -= 1
        if 0 <= i <= 9 and 0 <= j - 1 <= 9:
            if j > 0 and m[i][j - 1] == k - 1 and flagmove:
                flagmove = False
                i, j = i, j - 1
                the_path.append((i, j))
                k -= 1
        if 0 <= i + 1 <= 9 and 0 <= j <= 9:
            if i < len(m) - 1 and m[i + 1][j] == k - 1 and flagmove:
                flagmove = False
                i, j = i + 1, j
                the_path.append((i, j))
                k -= 1
        if 0 <= i <= 9 and 0 <= j + 1 <= 9:
            if j < len(m[i]) - 1 and m[i][j + 1] == k - 1 and flagmove:
                flagmove = False
                i, j = i, j + 1
                the_path.append((i, j))
                k -= 1

        flagmove = True

    the_path.reverse()
    # print(the_path)
    if m[end[0]][end[1]] > 0 and (m[end[0]][end[1]] + a not in allpath):
        allpath.setdefault(m[end[0]][end[1]] + a, the_path)

    # for i in m:
    #     print(i)
    # print()

    # m = [[] for i in range(8)]
    # for i in range(len(mstart)):
    #     for j in mstart[i]:
    #         m[i].append(j)
    # return the_path


get_path()
refresh_m()

secmas = [[] for i in range(len(m))]
for i in range(len(mas)):
    for j in mas[i]:
        secmas[i].append(j)

def move_figure(x, y, a, b: int, movefigure = 6) -> None:

    secmas[x][y], secmas[a][b] = 0, 1
    cycle(0, secmas)
    get_path(movefigure)
    secmas[x][y], secmas[a][b] = 1, 0
    mas = allpath[m[end[0]][end[1]] + movefigure]
    if type(mas[0]) == tuple:
        allpath[m[end[0]][end[1]] + movefigure] = [[(x, y), (a, b)], mas, [(a, b), (x, y)]]
    refresh_m()


# the_path = get_path()

if m[end[0]][end[1]] == 0:
    secmas = [[] for i in range(len(m))]
    for i in range(len(mas)):
        for j in mas[i]:
            secmas[i].append(j)

    if secmas[pos[0] - 1][pos[1]] == 1:
        if secmas[pos[0] - 2][pos[1]] == 0 and not (pos[0] - 2 == end[0] and pos[1] == end[1]):
            move_figure(pos[0] - 1, pos[1], pos[0] - 2, pos[1])
            # secmas[pos[0] - 1][pos[1]], secmas[pos[0] - 2][pos[1]] = 0, 1
            # cycle(0, secmas)
            # get_path(3)
            # secmas[pos[0] - 1][pos[1]], secmas[pos[0] - 2][pos[1]] = 1, 0
            # mas = allpath[m[end[0]][end[1]] + 3] #.insert(0, ((pos[0]) - 2, pos[1]))
            # allpath[m[end[0]][end[1]] + 3] = [((pos[0]) - 1, pos[1]), ((pos[0]) - 2, pos[1])], mas
            # refresh_m()
        if secmas[pos[0] - 2][pos[1] - 1] == 0 and not (pos[0] - 2 == end[0] and pos[1] - 1 == end[1]):
            move_figure(pos[0] - 1, pos[1], pos[0] - 2, pos[1] - 1)
        if secmas[pos[0] - 2][pos[1] + 1] == 0 and not (pos[0] - 2 == end[1] and pos[1] + 1 == end[1]):
            move_figure(pos[0] - 1, pos[1], pos[0] - 2, pos[1] + 1)

    if secmas[pos[0] - 1][pos[1] + 1] == 1 and secmas[pos[0] - 2][pos[1] + 2] == 0 and not (pos[0] - 2 == end[0] and pos[1] + 2 == end[1]):
        move_figure(pos[0] - 1, pos[1] + 1, pos[0] - 2, pos[1] + 2)

    if secmas[pos[0]][pos[1] + 1] == 1:
        if secmas[pos[0]][pos[1] + 2] == 0 and not (pos[0] == end[0] and pos[1] + 2 == end[1]):
            move_figure(pos[0], pos[1] + 1, pos[0], pos[1] + 2)
        if secmas[pos[0] - 1][pos[1] + 2] == 0 and not (pos[0] - 1 == end[0] and pos[1] + 2 == end[1]):
            move_figure(pos[0], pos[1] + 1, pos[0] - 1, pos[1] + 2)
        if secmas[pos[0] + 1][pos[1] + 2] == 0 and not (pos[0] + 1 == end[0] and pos[1] + 2 == end[1]):
            move_figure(pos[0], pos[1] + 1, pos[0] + 1, pos[1] + 2)

    if secmas[pos[0] + 1][pos[1] + 1] == 1 and secmas[pos[0] + 2][pos[1] + 2] == 0 and not (pos[0] + 2 == end[0] and pos[1] + 2 == end[1]):
        move_figure(pos[0] + 1, pos[1] + 1, pos[0] + 2, pos[1] + 2)

    if secmas[pos[0] + 1][pos[1]] == 1:
        if secmas[pos[0] + 2][pos[1]] == 0 and not (pos[0] + 2 == end[0] and pos[1] == end[1]):
            move_figure(pos[0] + 1, pos[1], pos[0] + 2, pos[1])
        if secmas[pos[0] + 2][pos[1] + 1] == 0 and not (pos[0] + 2 == end[0] and pos[1] + 1 == end[1]):
            move_figure(pos[0] + 1, pos[1], pos[0] + 2, pos[1] + 1)
        if secmas[pos[0] + 2][pos[1] - 1] == 0 and not (pos[0] + 2 == end[0] and pos[1] - 1 == end[1]):
            move_figure(pos[0] + 1, pos[1], pos[0] + 2, pos[1] - 1)

    if secmas[pos[0] + 1][pos[1] - 1] == 1 and secmas[pos[0] + 2][pos[1] - 2] == 0 and not (pos[0] + 2 == end[0] and pos[1] - 2 == end[1]):
        move_figure(pos[0] + 1, pos[1] - 1, pos[0] + 2, pos[1] - 2)

    if secmas[pos[0]][pos[1] - 1] == 1:
        if secmas[pos[0]][pos[1] - 2] == 1 and not (pos[0] == end[0] and pos[1] - 2 == end[1]):
            move_figure(pos[0], pos[1] - 1, pos[0], pos[1] - 2)
        if secmas[pos[0] + 1][pos[1] - 2] == 1 and not (pos[0] + 1 == end[0] and pos[1] - 2 == end[1]):
            move_figure(pos[0], pos[1] - 1, pos[0] + 1, pos[1] - 2)
        if secmas[pos[0] - 1][pos[1] - 2] == 1 and not (pos[0] - 1 == end[0] and pos[1] - 2 == end[1]):
            move_figure(pos[0], pos[1] - 1, pos[0] - 1, pos[1] - 2)

    if secmas[pos[0] - 1][pos[1] - 1] == 1 and secmas[pos[0] - 2][pos[1] - 2] == 0 and not (pos[0] - 2 == end[0] and pos[1] - 2 == end[1]):
        move_figure(pos[0] - 1, pos[1] - 1, pos[0] - 2, pos[1] - 2)


def printmas() -> None:
    # for i in m:
    #     print(i)
    # for i in the_path:
    #     print(i)
    # print(allpath)
    # for i in allpath.values():
    #     print(i)
    # print(allpath)
    minimal = min(allpath)
    # print(allpath[minimal])
    # print(allpath)
    massiv = []
    flagtype = False
    for i in allpath[minimal]:
        if type(i) == list:
            flagtype = True
    print(len(allpath[minimal]), allpath[minimal])
    if flagtype:
        mas = allpath[minimal][1]
        if len(mas) > 2:
            for i in range(len(mas) - 1):
                massiv.append([mas[i], mas[i + 1]])
        massiv.reverse()
        allpath[minimal].pop(1)
        for i in range(len(massiv)):
            allpath[minimal].insert(1, massiv[i])

    else:
        mas = allpath[minimal]
        if len(mas) > 2:
            for i in range(len(mas) - 1):
                massiv.append([mas[i], mas[i + 1]])
            allpath[minimal] = massiv
    print(allpath[minimal])


printmas()
