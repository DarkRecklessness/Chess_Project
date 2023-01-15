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
                    return True

            elif symbol.index(start[0]) + 1 == symbol.index(to[0]) and int(start[1]) + 1 == int(to[1]):
                if colorBoard[posVert[start] - 1][posHori[start] + 1] != '..':
                    return True

            elif symbol.index(start[0]) - 1 == symbol.index(to[0]) and int(start[1]) + 1 == int(to[1]):
                if colorBoard[posVert[start] - 1][posHori[start] - 1] != '..':
                    return True

            return False


        if color(colorBoard[posVert[start]][posHori[start]]) == 'Black':

            if symbol.index(start[0]) == symbol.index(to[0]) and int(start[1]) - 2 == int(to[1]) and int(start[1]) == 7 and colorBoard[posVert[start] + 2][posHori[start]] == '..':
                return True

            if symbol.index(start[0]) == symbol.index(to[0]) and int(start[1]) - 1 == int(to[1]):
                if colorBoard[posVert[start] + 1][posHori[start]] == '..':
                    return True

            elif symbol.index(start[0]) + 1 == symbol.index(to[0]) and int(start[1]) - 1 == int(to[1]):
                if colorBoard[posVert[start] + 1][posHori[start] + 1] != '..':
                    return True

            elif symbol.index(start[0]) - 1 == symbol.index(to[0]) and int(start[1]) - 1 == int(to[1]):
                if colorBoard[posVert[start] + 1][posHori[start] - 1] != '..':
                    return True

            return False



class Slon:


    def check_move(self, start, to):
        if check_diag(start, to):
            return True
        return False


def color(x):
    if x[0] == 'W':
        return 'White'
    else:
        return 'Black'


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

WH, BH = Horse(), Horse()
WP, BP = Pawn(), Pawn()
WS, BS = Slon(), Slon()


board = [
        #i----------------------------------------------
    ['BL', BH, BS, 'BQ', 'BK', BS, BH, 'BL'], #j
    [BP, BP, BP, BP, BP, BP, BP, BP], #|
    ['..', '..', '..', '..', '..', '..', '..', '..'], #|
    ['..', '..', '..', '..', '..', '..', '..', '..'], #|
    ['..', '..', '..', '..', '..', '..', '..', '..'], #|
    ['..', '..', '..', '..', '..', '..', '..', '..'], #|
    [WP, WP, WP, WP, WP, WP, WP, WP], #|
    ['WL', WH, WS, 'WQ', 'WK', WS, WH, 'WL']  #|
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
            xuy = []
            for j in colorBoard[i]:
                xuy.append(j)
            outputBoard.append(xuy)
        for i in outputBoard:
            i.reverse()
            print(" ".join(i))
    else:
        for i in colorBoard:
            print(" ".join(i))



frspos, secpos = input().split() # формат A2 A4
while frspos != 'esc' or secpos != 'esc':
    if board[posVert[frspos]][posHori[frspos]].check_move(frspos, secpos):
        chess_move(frspos, secpos)
    else:
        pass
    frspos, secpos = input().split()