mas = [
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 'S', 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0]
]


def posstart():

    for i in mas:
        for j in i:
            if j == 'S':
                fullmas = mas.index(i)
                return [fullmas, mas[fullmas].index(j)]


def posend():

    for i in mas:
        for j in i:
            if j == 'E':
                fullmas = mas.index(i)
                return [fullmas, mas[fullmas].index(j)]


m = []
for i in range(len(mas)):
    m.append([])
    for j in range(len(mas[i])):
        m[-1].append(0)
# i,j = start
pos = posstart()
m[pos[0]][pos[1]] = 1


def make_step(k: int) -> None:
  
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == k:
                try:    
                    if i > 0 and j < len(m[i]) - 1 and m[i - 1][j + 1] == 0 and mas[i - 1][j + 1] == 0:  # верх-право
                        m[i - 1][j + 1] = k + 1
                except IndexError:
                    pass
                try:    
                    if i > 0 and j > 0 and m[i - 1][j - 1] == 0 and mas[i - 1][j - 1] == 0: # верх-лево
                        m[i - 1][j - 1] = k + 1
                except IndexError:
                    pass
                try:    
                    if i < len(m) - 1 and j < len(m[i]) and m[i + 1][j + 1] == 0 and mas[i + 1][j + 1] == 0: # низ-право
                        m[i + 1][j + 1] = k + 1
                except IndexError: 
                    pass
                try:    
                    if i < len(m) - 1 and j > 0 and m[i + 1][j - 1] == 0 and mas[i + 1][j - 1] == 0: # низ-лево
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

end = [4, 4]

k = 0
while m[end[0]][end[1]] == 0:
    k += 1
    make_step(k)


def get_path() -> list:

    i, j = end[0], end[1]
    k = m[i][j]
    the_path = [(i,j)]

    while k > 1:

        if i > 0 and j < len(m[i]) - 1 and m[i - 1][j + 1] == k - 1:
            i, j = i - 1, j + 1
            the_path.append((i, j))
            k -= 1
        elif i > 0 and j > 0 and m[i - 1][j - 1] == k - 1:
            i, j = i - 1, j - 1
            the_path.append((i, j))
            k -= 1
        elif i < len(m) - 1 and j < len(m[i]) and m[i + 1][j + 1] == k - 1:
            i, j = i + 1, j + 1
            the_path.append((i, j))
            k -= 1
        elif i < len(m) - 1 and j > 0 and m[i + 1][j - 1] == k - 1:
            i, j = i + 1, j - 1
            the_path.append((i, j))
            k -= 1

        elif i > 0 and m[i - 1][j] == k - 1:
            i, j = i - 1, j
            the_path.append((i, j))
            k -= 1
        elif j > 0 and m[i][j - 1] == k - 1:
            i, j = i, j - 1
            the_path.append((i, j))
            k -= 1
        elif i < len(m) - 1 and m[i + 1][j] == k - 1:
            i, j = i + 1, j
            the_path.append((i, j))
            k -= 1
        elif j < len(m[i]) - 1 and m[i][j + 1] == k - 1:
            i, j = i, j + 1
            the_path.append((i, j))
            k -= 1

    the_path.reverse()
    return the_path

the_path = get_path()


def printmas() -> None:

    for i in m:
        print(i)
    for i in the_path:
        print(i)

printmas()
print(m[end[0]][end[1]] - 1)
