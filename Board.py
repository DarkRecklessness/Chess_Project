# задаем начальную расстановку за БЕЛЫХ
symbol = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


class Horse:


    def check_move(self, start, to): #B1 C3     +A+2:+A-2:   -A+2:-A-2:     +2A+1:+2A-1:-2A+1:-2A-1

        try:
            if symbol.index(start[0]) + 1 == symbol.index(to[0]) and abs(int(start[1]) - int(to[1])) == 2:
                return True
        except IndexError:
            pass
        try:
            if symbol.index(start[0]) - 1 == symbol.index(to[0]) and abs(int(start[1]) - int(to[1])) == 2:
                return True
        except IndexError:
            pass
        try:
            if symbol.index(start[0]) + 2 == symbol.index(to[0]) and abs(int(start[1]) - int(to[1])) == 1:
                return True
        except IndexError:
            pass
        try:
            if symbol.index(start[0]) - 2 == symbol.index(to[0]) and abs(int(start[1]) - int(to[1])) == 1:
                return True
        except IndexError:
            pass
        return False


class Pawn:


    def check_move(self, start, to):

        if color(colorBoard[posVert[start]][posHori[start]]) == 'White':

            if symbol.index(start[0]) == symbol.index(to[0]) and int(start[1]) + 2 == int(to[1]) and int(start[1]) == 2 and colorBoard[posVert[start] - 2][posHori[start]] == '..':
                return True

            if symbol.index(start[0]) == symbol.index(to[0]) and int(start[1]) + 1 == int(to[1]):
                if colorBoard[posVert[start] - 1][posHori[start]] == '..':
                    if int(to[1]) == 8:
                        Ghost_Pawn('White', start)
                    return True

            if symbol.index(start[0]) + 1 == symbol.index(to[0]) and int(start[1]) + 1 == int(to[1]):
                if colorBoard[posVert[start] - 1][posHori[start] + 1] != '..':
                    if int(to[1]) == 8:
                        Ghost_Pawn('White', start)
                    return True

            if symbol.index(start[0]) - 1 == symbol.index(to[0]) and int(start[1]) + 1 == int(to[1]):
                if colorBoard[posVert[start] - 1][posHori[start] - 1] != '..':
                    if int(to[1]) == 8:
                        Ghost_Pawn('White', start)
                    return True

            return False


        if color(colorBoard[posVert[start]][posHori[start]]) == 'Black':

            if symbol.index(start[0]) == symbol.index(to[0]) and int(start[1]) - 2 == int(to[1]) and int(start[1]) == 7 and colorBoard[posVert[start] + 2][posHori[start]] == '..':
                return True

            if symbol.index(start[0]) == symbol.index(to[0]) and int(start[1]) - 1 == int(to[1]):
                if colorBoard[posVert[start] + 1][posHori[start]] == '..':
                    if int(to[1]) == 1:
                        Ghost_Pawn('Black', start)
                    return True

            if symbol.index(start[0]) + 1 == symbol.index(to[0]) and int(start[1]) - 1 == int(to[1]):
                if colorBoard[posVert[start] + 1][posHori[start] + 1] != '..':
                    if int(to[1]) == 1:
                        Ghost_Pawn('Black', start)
                    return True

            if symbol.index(start[0]) - 1 == symbol.index(to[0]) and int(start[1]) - 1 == int(to[1]):
                if colorBoard[posVert[start] + 1][posHori[start] - 1] != '..':
                    if int(to[1]) == 1:
                        Ghost_Pawn('Black', start)
                    return True

            return False



class Slon:


    def check_move(self, start, to):
        if check_diag(start, to):
            return True
        return False


class Rock:


    def check_move(self, start, to):
        if check_line(start, to):
            return True
        return False


class Queen:


    def check_move(self, start, to):
        if check_diag(start, to) or check_line(start, to):
            return True
        return False


class King:


    def check_move(self, start, to):

        if color(colorBoard[posVert[start]][posHori[start]]) == 'White':
            if symbol.index(start[0]) + 2 == symbol.index(to[0]) and int(start[1]) == int(to[1]) and flagWK and flagWL2:
                if board[posVert[start]][posHori[start] + 1] == '..' and board[posVert[start]][posHori[start] + 2] == '..':
                    board[7][7], board[7][5] = board[7][5], board[7][7]
                    colorBoard[7][7], colorBoard[7][5] = colorBoard[7][5], colorBoard[7][7]
                    return True
            if symbol.index(start[0]) - 2 == symbol.index(to[0]) and int(start[1]) == int(to[1]) and flagWK and flagWL1:
                if board[posVert[start]][posHori[start] - 1] == '..' and board[posVert[start]][posHori[start] - 2] == '..' and board[posVert[start]][posHori[start] - 3]:
                    board[7][0], board[7][3] = board[7][3], board[7][0]
                    colorBoard[7][0], colorBoard[7][3] = colorBoard[7][3], colorBoard[7][0]
                    return True
        else:
            if symbol.index(start[0]) + 2 == symbol.index(to[0]) and int(start[1]) == int(to[1]) and flagBK and flagBL2:
                if board[posVert[start]][posHori[start] + 1] == '..' and board[posVert[start]][posHori[start] + 2] == '..':
                    board[0][7], board[0][5] = board[0][5], board[0][7]
                    colorBoard[0][7], colorBoard[0][5] = colorBoard[0][5], colorBoard[0][7]
                    return True
            if symbol.index(start[0]) - 2 == symbol.index(to[0]) and int(start[1]) == int(to[1]) and flagBK and flagBL1:
                if board[posVert[start]][posHori[start] - 1] == '..' and board[posVert[start]][posHori[start] - 2] == '..' and board[posVert[start]][posHori[start] - 3]:
                    board[0][0], board[0][3] = board[0][3], board[0][0]
                    colorBoard[0][0], colorBoard[0][3] = colorBoard[0][3], colorBoard[0][0]
                    return True

        try:
            if int(to[1]) - int(start[1]) == 1 and (symbol.index(start[0]) == symbol.index(to[0]) or symbol.index(to[0]) - symbol.index(start[0]) == 1 or symbol.index(start[0]) - symbol.index(to[0]) == 1):
                return True
        except IndexError:
            pass
        try:
            if int(to[1]) == int(start[1]) and (symbol.index(to[0]) - symbol.index(start[0]) == 1 or symbol.index(start[0]) - symbol.index(to[0]) == 1):
                return True
        except IndexError:
            pass
        try:
            if int(start[1]) - int(to[1]) == 1 and (symbol.index(start[0]) == symbol.index(to[0]) or symbol.index(to[0]) - symbol.index(start[0]) == 1 or symbol.index(start[0]) - symbol.index(to[0]) == 1):
                return True
        except IndexError:
            pass
        return False

def color(x):
    if x[0] == 'W':
        return 'White'
    else:
        return 'Black'


def Ghost_Pawn(color, start):

    if color == 'White':
        figure = input('Select figure: WQ/WH >>> ')
        if figure == 'WQ':
            board[posVert[start]][posHori[start]] = WQ
            colorBoard[posVert[start]][posHori[start]] = 'WQ'
        if figure == 'WH':
            board[posVert[start]][posHori[start]] = WH
            colorBoard[posVert[start]][posHori[start]] = 'WH'

    if color == 'Black':
        figure = input('Select figure: BQ/BH >>> ')
        if figure == 'BQ':
            board[posVert[start]][posHori[start]] = BQ
            colorBoard[posVert[start]][posHori[start]] = 'BQ'
        if figure == 'BH':
            board[posVert[start]][posHori[start]] = BH
            colorBoard[posVert[start]][posHori[start]] = 'BH'


def check_diag(start, to):
    try:
        if symbol.index(start[0]) == symbol.index(to[0]) - (int(to[1]) - int(start[1])) and start[1] < to[1]: ## C1 E3: 2 == 4 - (2) напр право-верх
            for i in range(1, (int(to[1])) - int(start[1])): # range(2, 6) board[5][2]
                if board[posVert[start] - i][posHori[start] + i] != '..':
                    return False
            return True
    except IndexError:
        pass
    try:
        if symbol.index(start[0]) == symbol.index(to[0]) - (int(start[1]) - int(to[1])) and start[1] > to[1]: ## A3 C1: 0 == 2 - (2) напр право-низ
            for i in range(1, int(start[1]) - int(to[1])):
                if board[posVert[start] + i][posHori[start] + i] != '..':
                    return False
            return True
    except IndexError:
        pass
    try:
        if symbol.index(start[0]) == symbol.index(to[0]) + (int(start[1]) - int(to[1])): ## D4 B2: 3 == 1 + (2) напр лево-низ
            for i in range(1, int(start[1]) - int(to[1])): # i = 1
                if board[posVert[start] + i][posHori[start] - i] != '..':
                    return False
            return True
    except IndexError:
        pass
    try:
        if symbol.index(start[0]) == symbol.index(to[0]) + (int(to[1]) - int(start[1])): ## C1 A3: 2 == 0 + (2) напр лево-верх
            for i in range(1, (int(to[1])) - int(start[1])):
                if board[posVert[start] - i][posHori[start] - i] != '..':
                    return False
            return True
    except IndexError:
        pass
    return False


def check_line(start, to):

    try:
        if symbol.index(start[0]) == symbol.index(to[0]) and int(start[1]) < int(to[1]):#верх
            for i in range(1, int(to[1]) - int(start[1])):
                if board[posVert[start] - i][posHori[start]] != '..':
                    return False
            return True
    except IndexError:
        pass

    try:
        if symbol.index(start[0]) == symbol.index(to[0]) and int(start[1]) > int(to[1]): #низ
            for i in range(1, int(start[1]) - int(to[1])):
                if board[posVert[start] + i][posHori[start]] != '..':
                    return False
            return True
    except IndexError:
        pass

    try:
        if symbol.index(start[0]) < symbol.index(to[0]) and int(start[1]) == int(to[1]): #право
            for i in range(1, symbol.index(to[0]) - symbol.index(start[0])):
                if board[posVert[start]][posHori[start] + i] != '..':
                    return False
            return True
    except IndexError:
        pass

    try:
        if symbol.index(start[0]) > symbol.index(to[0]) and int(start[1]) == int(to[1]): #лево
            for i in range(1, symbol.index(start[0]) - symbol.index(to[0])):
                if board[posVert[start]][posHori[start] - i] != '..':
                    return False
            return True
    except IndexError:
        pass

    return False


WH, BH = Horse(), Horse()
WP, BP = Pawn(), Pawn()
WS, BS = Slon(), Slon()
WL1, WL2, BL1, BL2 = Rock(), Rock(), Rock(), Rock()
WQ, BQ = Queen(), Queen()
WK, BK = King(), King()


flagWL1 = True
flagWL2 = True
flagBL1 = True
flagBL2 = True
flagWK = True
flagBK = True



board = [
    #i----------------------------------------------
    [BL1, BH, BS, BQ, BK, BS, BH, BL2], #j
    [BP, BP, BP, BP, BP, BP, BP, BP], #|
    ['..', '..', '..', '..', '..', '..', '..', '..'], #|
    ['..', '..', '..', '..', '..', '..', '..', '..'], #|
    ['..', '..', '..', '..', '..', '..', '..', '..'], #|
    ['..', '..', '..', '..', '..', '..', '..', '..'], #|
    [WP, WP, WP, WP, WP, WP, WP, WP], #|
    [WL1, WH, WS, WQ, WK, WS, WH, WL2]  #|
]

colorBoard = [
    ['BL', 'BH', 'BS', 'BQ', 'BK', 'BS', 'BH', 'BL'],
    ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
    ['..', '..', '..', '..', '..', '..', '..', '..'],
    ['..', '..', '..', '..', '..', '..', '..', '..'],
    ['..', '..', '..', '..', '..', '..', '..', '..'],
    ['..', '..', '..', '..', '..', '..', '..', '..'],
    ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
    ['WL', 'WH', 'WS', 'WQ', 'WK', 'WS', 'WH', 'WL']
]


posHori = {}
posVert = {}
for i in range(8):
    count = 1
    for j in range(7, -1, -1):
        posHori.setdefault(f'{symbol[0] + str(count)}', i)
        posVert.setdefault(f'{symbol[0] + str(count)}', j)
        count += 1
    symbol.pop(0)
symbol = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

colorselect = input('Select side>>> ')


def chess_move(frspos, secpos):

    if board[posVert[secpos]][posHori[secpos]] == '..':
        board[posVert[frspos]][posHori[frspos]], board[posVert[secpos]][posHori[secpos]] = board[posVert[secpos]][
                                                                                               posHori[secpos]], \
                                                                                           board[posVert[frspos]][
                                                                                               posHori[frspos]]
        colorBoard[posVert[frspos]][posHori[frspos]], colorBoard[posVert[secpos]][posHori[secpos]] = colorBoard[posVert[secpos]][
                                                                                               posHori[secpos]], \
                                                                                           colorBoard[posVert[frspos]][
                                                                                               posHori[frspos]]

    elif colorBoard[posVert[frspos]][posHori[frspos]][0] == colorBoard[posVert[secpos]][posHori[secpos]][0]:
        print('Больной?')
    else:
        board[posVert[secpos]][posHori[secpos]] = '..'
        colorBoard[posVert[secpos]][posHori[secpos]] = '..'
        board[posVert[frspos]][posHori[frspos]], board[posVert[secpos]][posHori[secpos]] = board[posVert[secpos]][
                                                                                               posHori[secpos]], \
                                                                                           board[posVert[frspos]][
                                                                                               posHori[frspos]]
        colorBoard[posVert[frspos]][posHori[frspos]], colorBoard[posVert[secpos]][posHori[secpos]] = colorBoard[posVert[secpos]][
                                                                                               posHori[secpos]], \
                                                                                           colorBoard[posVert[frspos]][
                                                                                               posHori[frspos]]

    outputBoard = []
    if colorselect == 'Black':
        for i in range(len(colorBoard) - 1, -1, -1):
            mas = []
            for j in colorBoard[i]:
                mas.append(j)
            outputBoard.append(mas)
        for i in outputBoard:
            i.reverse()
            print(" ".join(i))
    else:
        for i in colorBoard:
            print(" ".join(i))



frspos, secpos = input().split()# формат A2 A4
while frspos != 'esc' or secpos != 'esc':
    if board[posVert[frspos]][posHori[frspos]].check_move(frspos, secpos):
        chess_move(frspos, secpos)
        if board[posVert[secpos]][posHori[secpos]] == WK: flagWK = False
        if board[posVert[secpos]][posHori[secpos]] == BK: flagBK = False
        if board[posVert[secpos]][posHori[secpos]] == WL1: flagWL1 = False
        if board[posVert[secpos]][posHori[secpos]] == WL2: flagWL2 = False
        if board[posVert[secpos]][posHori[secpos]] == BL1: flagBL1 = False
        if board[posVert[secpos]][posHori[secpos]] == BL2: flagBL2 = False
    else:
        print('incorrect path')
    frspos, secpos = input().split()