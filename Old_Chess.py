'''







Используется изменённая версия функции в библиотеке SpeechRecognition
Редактированная функция recognize_google - https://github.com/DarkRecklessness/Chess_Project/blob/main/recognize_google








'''



from stockfish import Stockfish
import speech_recognition as sp
import keyboard
import time

stockfish = Stockfish("C:\\Users\\Denis\\Desktop\\stockfish_15.1_win_x64_avx2\\stockfish-windows-2022-x86-64-avx2.exe")
stockfish.set_skill_level(20)
stockfish.set_depth(10)
stockfish.set_elo_rating(3200)
# print(stockfish.get_parameters())

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

        global flagp2, flagpvz

        if color(colorBoard[posVert[start]][posHori[start]]) == 'White':

            if symbol.index(start[0]) == symbol.index(to[0]) and int(start[1]) + 2 == int(to[1]) and int(start[1]) == 2 and colorBoard[posVert[start] - 2][posHori[start]] == '..':
                flagp2 = str(to).lower()
                flagpvz = 0
                return True

            if symbol.index(start[0]) == symbol.index(to[0]) and int(start[1]) + 1 == int(to[1]):
                if colorBoard[posVert[start] - 1][posHori[start]] == '..':
                    if int(to[1]) == 8:
                        Ghost_Pawn('White', start)
                    flagpvz = 0
                    return True

            if symbol.index(start[0]) + 1 == symbol.index(to[0]) and int(start[1]) + 1 == int(to[1]):
                if colorBoard[posVert[start] - 1][posHori[start] + 1] != '..':
                    if int(to[1]) == 8:
                        Ghost_Pawn('White', start)
                    flagpvz = 0
                    return True
                elif movep2 == f'{to[0]}{int(to[1]) - 1}':
                    enpassant(movep2)
                    return True

            if symbol.index(start[0]) - 1 == symbol.index(to[0]) and int(start[1]) + 1 == int(to[1]):
                if colorBoard[posVert[start] - 1][posHori[start] - 1] != '..':
                    if int(to[1]) == 8:
                        Ghost_Pawn('White', start)
                    flagpvz = 0
                    return True
                elif movep2 == f'{to[0]}{int(to[1]) - 1}':
                    enpassant(movep2)
                    return True

            return False


        if color(colorBoard[posVert[start]][posHori[start]]) == 'Black':

            if symbol.index(start[0]) == symbol.index(to[0]) and int(start[1]) - 2 == int(to[1]) and int(start[1]) == 7 and colorBoard[posVert[start] + 2][posHori[start]] == '..':
                flagp2 = str(to).lower()
                flagpvz = 0
                return True

            if symbol.index(start[0]) == symbol.index(to[0]) and int(start[1]) - 1 == int(to[1]):
                if colorBoard[posVert[start] + 1][posHori[start]] == '..':
                    if int(to[1]) == 1:
                        Ghost_Pawn('Black', start)
                    flagpvz = 0
                    return True

            if symbol.index(start[0]) + 1 == symbol.index(to[0]) and int(start[1]) - 1 == int(to[1]):
                if colorBoard[posVert[start] + 1][posHori[start] + 1] != '..':
                    if int(to[1]) == 1:
                        Ghost_Pawn('Black', start)
                    flagpvz = 0
                    return True
                elif movep2 == f'{to[0]}{int(to[1]) + 1}':
                    enpassant(movep2)
                    return True

            if symbol.index(start[0]) - 1 == symbol.index(to[0]) and int(start[1]) - 1 == int(to[1]):
                if colorBoard[posVert[start] + 1][posHori[start] - 1] != '..':
                    if int(to[1]) == 1:
                        Ghost_Pawn('Black', start)
                    flagpvz = 0
                    return True
                elif movep2 == f'{to[0]}{int(to[1]) + 1}':
                    enpassant(movep2)
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
                    stockfishBoard[7][7], stockfishBoard[7][5] = stockfishBoard[7][5], stockfishBoard[7][7]
                    return True
            if symbol.index(start[0]) - 2 == symbol.index(to[0]) and int(start[1]) == int(to[1]) and flagWK and flagWL1:
                if board[posVert[start]][posHori[start] - 1] == '..' and board[posVert[start]][posHori[start] - 2] == '..' and board[posVert[start]][posHori[start] - 3]:
                    board[7][0], board[7][3] = board[7][3], board[7][0]
                    colorBoard[7][0], colorBoard[7][3] = colorBoard[7][3], colorBoard[7][0]
                    stockfishBoard[7][0], stockfishBoard[7][3] = stockfishBoard[7][3], stockfishBoard[7][0]
                    return True
        else:
            if symbol.index(start[0]) + 2 == symbol.index(to[0]) and int(start[1]) == int(to[1]) and flagBK and flagBL2:
                if board[posVert[start]][posHori[start] + 1] == '..' and board[posVert[start]][posHori[start] + 2] == '..':
                    board[0][7], board[0][5] = board[0][5], board[0][7]
                    colorBoard[0][7], colorBoard[0][5] = colorBoard[0][5], colorBoard[0][7]
                    stockfishBoard[0][7], stockfishBoard[0][5] = stockfishBoard[0][5], stockfishBoard[0][7]
                    return True
            if symbol.index(start[0]) - 2 == symbol.index(to[0]) and int(start[1]) == int(to[1]) and flagBK and flagBL1:
                if board[posVert[start]][posHori[start] - 1] == '..' and board[posVert[start]][posHori[start] - 2] == '..' and board[posVert[start]][posHori[start] - 3]:
                    board[0][0], board[0][3] = board[0][3], board[0][0]
                    colorBoard[0][0], colorBoard[0][3] = colorBoard[0][3], colorBoard[0][0]
                    stockfishBoard[0][0], stockfishBoard[0][3] = stockfishBoard[0][3], stockfishBoard[0][0]
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


def check_a():


    sr = sp.Recognizer()
    sr.pause_threshold = 0.7
    #sr.phrase_threshold = 0.2

    with sp.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        print("start")
        # st_time = time.time()
        audio = sr.listen(source=mic)
        aa = ''
        #end_time = time.time()
        #while (end_time - st_time) < 4:
        try:
            query = sr.recognize_google(audio_data=audio, language='ru-Ru')
            aa = query
            #end_time = time.time()
        except("speech_recognition.UnknownValueError"):
            print("Repeat, pls")
            st()
        #end_time = time.time()

    if aa == '' or aa == ' ':
        print("Repeat, plssss")
        st()
    else:
        #print(aa)
        return aa


def conf():

    voice = check_a()
    #print(voice)
    st = str(voice) + ' '
    voice = ''
    st2 = ''
    mas = []
    for i in range(len(st)):
        if st[i] == ' ':
            mas.append(st2)
            st2 = ' '
        else:
            st2 = st2 + st[i]
        #print(st[i])
    #print((mas))
    for i in range(len(mas)):

        if mas[i] == "опять":
            mas[i] = "A5"
        if mas[i] == "а":
            mas[i] = "A"
        if mas[i] == "А":
            mas[i] = "A"
        if mas[i] == "два":
            mas[i] = "2"
        if mas[i] == "едва":
            mas[i] = "E2"
        #else:
        #    pass
    st = ''
    for i in range(len(mas)):
        st = st + mas[i]

    st2 = ''
    for i in range(len(st)):
        if st[i] == 'а' or st[i] == 'А':
            st2 += 'A'
        elif st[i] == 'б' or st[i] == 'Б':
            st2 += 'B'
        elif st[i] == 'с' or st[i] == 'С':
            st2 += 'C'
        elif st[i] == 'д' or st[i] == 'Д':
            st2 += 'D'
        elif st[i] == 'е' or st[i] == 'Е':
            st2 += 'E'
        else:
            st2 += st[i]


    for i in range(len(st2)):
        voice = voice + st2[i]

    if (len(voice)) == 4:
        # pass
        voice = voice.upper()
        voice = voice[:2] + ' ' + voice[2:]
        #print(voice)
    else:
        pass
    #print(voice + "hghghghg")
    voice = voice.upper()
    return voice



def st():
    print("Enter g")
    while True:
        if keyboard.record("g"):
            time.sleep(0.4)
            return conf()
            #break


def color(x):
    if x[0] == 'W':
        return 'White'
    else:
        return 'Black'

def is_valid_move(x, board):

    colorFigure = colorselect

    for i in range(1, min(7 - symbol.index(x[0]), 8 - int(x[1])) + 1): #F5 диагональ верх-право
        if board[posVert[x] - i][posHori[x] + i] != '..':
            if colorFigure == 'White' and (board[posVert[x] - i][posHori[x] + i] in (BS, BQ)):
                return False
            elif colorFigure == 'Black' and (board[posVert[x] - i][posHori[x] + i] in (WS, WQ)):
                return False
            break

    for i in range(1, min(symbol.index(x[0]), 8 - int(x[1])) + 1): #диагональ верх-лево
        if board[posVert[x] - i][posHori[x] - i] != '..':
            if colorFigure == 'White' and (board[posVert[x] - i][posHori[x] - i] in (BS, BQ)):
                return False
            elif colorFigure == 'Black' and (board[posVert[x] - i][posHori[x] - i] in (WS, WQ)):
                return False
            break

    for i in range(1, min(7 - symbol.index(x[0]), int(x[1]) - 1) + 1): #диагональ низ-право
        if board[posVert[x] + i][posHori[x] + i] != '..':
            if colorFigure == 'White' and (board[posVert[x] + i][posHori[x] + i] in (BS, BQ)):
                return False
            elif colorFigure == 'Black' and (board[posVert[x] + i][posHori[x] + i] in (WS, WQ)):
                return False
            break

    for i in range(1, min(symbol.index(x[0]), int(x[1]) - 1) + 1): #диагональ низ-лево
        if board[posVert[x] + i][posHori[x] - i] != '..':
            if colorFigure == 'White' and (board[posVert[x] + i][posHori[x] - i] in (BS, BQ)):
                return False
            elif colorFigure == 'Black' and (board[posVert[x] + i][posHori[x] - i] in (WS, WQ)):
                return False
            break


    for i in range(1, int(x[1])): #низ
        if board[posVert[x] + i][posHori[x]] != '..':
            if colorFigure == 'White' and (board[posVert[x] + i][posHori[x]] in (BL1, BL2, BQ)):
                return False
            elif colorFigure == 'Black' and (board[posVert[x] + i][posHori[x]] in (WL1, WL2, WQ)):
                return False
            break

    for i in range(1, 8 - int(x[1]) + 1): #верх
        if board[posVert[x] - i][posHori[x]] != '..':
            if colorFigure == 'White' and (board[posVert[x] - i][posHori[x]] in (BL1, BL2, BQ)):
                return False
            elif colorFigure == 'Black' and (board[posVert[x] - i][posHori[x]] in (WL1, WL2, WQ)):
                return False
            break

    for i in range(1, 7 - symbol.index(x[0]) + 1): #право
        if board[posVert[x]][posHori[x] + i] != '..':
            if colorFigure == 'White' and (board[posVert[x]][posHori[x] + i] in (BL1, BL2, BQ)):
                return False
            elif colorFigure == 'Black' and (board[posVert[x]][posHori[x] + i] in (WL1, WL2, WQ)):
                return False
            break

    for i in range(1, symbol.index(x[0]) + 1): #лево
        if board[posVert[x]][posHori[x] - i] != '..':
            if colorFigure == 'White' and (board[posVert[x]][posHori[x] - i] in (BL1, BL2, BQ)):
                return False
            elif colorFigure == 'Black' and (board[posVert[x]][posHori[x] - i] in (WL1, WL2, WQ)):
                return False
            break


    if colorFigure == 'White' and posVert[x] != 0:
        if posHori[x] < 7:
            if BP == board[posVert[x] - 1][posHori[x] + 1]:
                return False
        if posHori[x] > 0:
            if BP == board[posVert[x] - 1][posHori[x] - 1]:
                return False
    elif colorFigure == 'Black' and posVert[x] != 7:
        if posHori[x] < 7:
            if WP == board[posVert[x] + 1][posHori[x] + 1]:
                return False
        if posHori[x] > 0:
            if WP == board[posVert[x] + 1][posHori[x] - 1]:
                return False

    if colorFigure == 'White':
        try:
            if BH == board[posVert[x] - 2][posHori[x] + 1] and posVert[x] - 2 >= 0 and posHori[x] + 1 >= 0: return False
        except:
            pass
        try:
            if BH == board[posVert[x] - 1][posHori[x] + 2] and posVert[x] - 1 >= 0 and posHori[x] + 2 >= 0: return False
        except:
            pass
        try:
            if BH == board[posVert[x] + 1][posHori[x] + 2] and posVert[x] + 1 >= 0 and posHori[x] + 2 >= 0: return False
        except:
            pass
        try:
            if BH == board[posVert[x] + 2][posHori[x] + 1] and posVert[x] + 2 >= 0 and posHori[x] + 1 >= 0: return False
        except:
            pass
        try:
            if BH == board[posVert[x] + 2][posHori[x] - 1] and posVert[x] + 2 >= 0 and posHori[x] - 1 >= 0: return False
        except:
            pass
        try:
            if BH == board[posVert[x] + 1][posHori[x] - 2] and posVert[x] + 1 >= 0 and posHori[x] - 2 >= 0: return False
        except:
            pass
        try:
            if BH == board[posVert[x] - 1][posHori[x] - 2] and posVert[x] - 1 >= 0 and posHori[x] - 2 >= 0: return False
        except:
            pass
        try:
            if BH == board[posVert[x] - 2][posHori[x] - 1] and posVert[x] - 2 >= 0 and posHori[x] - 1 >= 0: return False
        except:
            pass

    if colorFigure == 'Black':
        try:
            if WH == board[posVert[x] - 2][posHori[x] + 1] and posVert[x] - 2 >= 0 and posHori[x] + 1 >= 0: return False
        except: pass
        try:
            if WH == board[posVert[x] - 1][posHori[x] + 2] and posVert[x] - 1 >= 0 and posHori[x] + 2 >= 0: return False
        except: pass
        try:
            if WH == board[posVert[x] + 1][posHori[x] + 2] and posVert[x] + 1 >= 0 and posHori[x] + 2 >= 0: return False
        except: pass
        try:
            if WH == board[posVert[x] + 2][posHori[x] + 1] and posVert[x] + 2 >= 0 and posHori[x] + 1 >= 0: return False
        except: pass
        try:
            if WH == board[posVert[x] + 2][posHori[x] - 1] and posVert[x] + 2 >= 0 and posHori[x] - 1 >= 0: return False
        except: pass
        try:
            if WH == board[posVert[x] + 1][posHori[x] - 2] and posVert[x] + 1 >= 0 and posHori[x] - 2 >= 0: return False
        except: pass
        try:
            if WH == board[posVert[x] - 1][posHori[x] - 2] and posVert[x] - 1 >= 0 and posHori[x] - 2 >= 0: return False
        except: pass
        try:
            if WH == board[posVert[x] - 2][posHori[x] - 1] and posVert[x] - 2 >= 0 and posHori[x] - 1 >= 0: return False
        except: pass

    return True

def Ghost_Pawn(colorghost, start):

    global move
    global board, colorBoard, stockfishBoard

    if colorghost == 'White':
        try:
            if not (move[4].isdigit()):
                figure = 'W' + move[4].upper()
        except IndexError:
            figure = input('Select figure: WQ/WH >>> ')
        if figure in ('WQ', 'WB', 'WR'):
            board[posVert[start]][posHori[start]] = WQ
            colorBoard[posVert[start]][posHori[start]] = 'WQ'
            stockfishBoard[posVert[start]][posHori[start]] = 'Q'
        elif figure in ('WH', 'WN'):
            board[posVert[start]][posHori[start]] = WH
            colorBoard[posVert[start]][posHori[start]] = 'WH'
            stockfishBoard[posVert[start]][posHori[start]] = 'K'

    if colorghost == 'Black':
        try:
            if not (move[4].isdigit()):
                figure = 'B' + move[4].upper()
        except IndexError:
            figure = input('Select figure: WQ/WH >>> ')
        if figure in ('BQ', 'BB', 'BR'):
            board[posVert[start]][posHori[start]] = BQ
            colorBoard[posVert[start]][posHori[start]] = 'BQ'
            stockfishBoard[posVert[start]][posHori[start]] = 'q'
        elif figure in ('BH', 'BN'):
            board[posVert[start]][posHori[start]] = BH
            colorBoard[posVert[start]][posHori[start]] = 'BH'
            stockfishBoard[posVert[start]][posHori[start]] = 'k'


def enpassant(movep2):

    global board, colorBoard, stockfishBoard

    board[posVert[movep2]][posHori[movep2]] = '..'
    colorBoard[posVert[movep2]][posHori[movep2]] = '..'
    stockfishBoard[posVert[movep2]][posHori[movep2]] = '.'


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


flagK, flagQ, flagk, flagq = True, True, True, True
flagp2 = '-'
flagpvz = 0
movep2 = ''


def fen():

    fen = ''
    for i in stockfishBoard:
        count = 0
        for j in i:
            if j == '.':
                count += 1
            elif count != 0:
                fen += str(count)
                count = 0
            if j != '.':
                fen += j
        if count != 0:
            fen += str(count)
        fen += '/'
    fen = fen[:-1]

    if count_move % 2 == 1:
        fen += ' w '
    else:
        fen += ' b '

    if flagK == True:
        fen += 'K'
    if flagQ == True:
        fen += 'Q'
    if flagk == True:
        fen += 'k'
    if flagq == True:
        fen += 'q'
    fen += ' '
    fen += flagp2
    fen += ' '
    fen += str(flagpvz)
    fen += ' '
    fen += str(count_move)

    return fen


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


stockfishBoard = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
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

    global flagpvz
    global count_move

    if board[posVert[secpos]][posHori[secpos]] == '..':
        board[posVert[frspos]][posHori[frspos]], board[posVert[secpos]][posHori[secpos]] = board[posVert[secpos]][
                                                                                               posHori[secpos]], \
                                                                                           board[posVert[frspos]][
                                                                                               posHori[frspos]]
        colorBoard[posVert[frspos]][posHori[frspos]], colorBoard[posVert[secpos]][posHori[secpos]] = colorBoard[posVert[secpos]][
                                                                                               posHori[secpos]], \
                                                                                           colorBoard[posVert[frspos]][
                                                                                               posHori[frspos]]
        stockfishBoard[posVert[frspos]][posHori[frspos]], stockfishBoard[posVert[secpos]][posHori[secpos]] = \
        stockfishBoard[posVert[secpos]][
            posHori[secpos]], \
        stockfishBoard[posVert[frspos]][
            posHori[frspos]]

        count_move += 1

    elif colorBoard[posVert[frspos]][posHori[frspos]][0] == colorBoard[posVert[secpos]][posHori[secpos]][0]:
        print('incorrect path')
    else:
        board[posVert[secpos]][posHori[secpos]] = '..'
        colorBoard[posVert[secpos]][posHori[secpos]] = '..'
        stockfishBoard[posVert[secpos]][posHori[secpos]] = '.'
        board[posVert[frspos]][posHori[frspos]], board[posVert[secpos]][posHori[secpos]] = board[posVert[secpos]][
                                                                                               posHori[secpos]], \
                                                                                           board[posVert[frspos]][
                                                                                               posHori[frspos]]
        colorBoard[posVert[frspos]][posHori[frspos]], colorBoard[posVert[secpos]][posHori[secpos]] = colorBoard[posVert[secpos]][
                                                                                               posHori[secpos]], \
                                                                                           colorBoard[posVert[frspos]][
                                                                                               posHori[frspos]]
        stockfishBoard[posVert[frspos]][posHori[frspos]], stockfishBoard[posVert[secpos]][posHori[secpos]] = \
        stockfishBoard[posVert[secpos]][
            posHori[secpos]], \
        stockfishBoard[posVert[frspos]][
            posHori[frspos]]

        count_move += 1
        flagpvz = 0

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
        # print(fen())
    else:
        for i in colorBoard:
            print(" ".join(i))
        # print(fen())


count_move = 1

# if colorselect != 'Black': frspos, secpos = input().split()
# else:
#     stockfish.set_fen_position(fen())
#     move = stockfish.get_best_move().upper()
#     frspos = move[:2]
#     secpos = move[2::1]
#     print(frspos, secpos)

posWK = 'E1'
posBK = 'E8'
while True:

    if colorselect == 'White' and count_move % 2 == 1: # and count_move % 2 == 1
        try:
            stockfish.set_fen_position(fen())
            if stockfish.get_best_move() == None:
                print('checkmate!')
                exit()
            ee = st()
            frspos, secpos = ee[:2], ee[3:5]
            #print(frspos)
            #print(secpos)
            print(frspos, secpos)
            if board[posVert[frspos]][posHori[frspos]] == WK:
                if not is_valid_move(secpos, board):
                    print('incorrect path')
                    continue
            elif colorBoard[posVert[frspos]][posHori[frspos]][0] != 'W':
                print('incorrect path')
                continue
            else:
                board2 = []
                for i in board:
                    mas = []
                    for j in i:
                        mas.append(j)
                    board2.append(mas)
                board2[posVert[secpos]][posHori[secpos]] = '..'
                board2[posVert[frspos]][posHori[frspos]], board2[posVert[secpos]][posHori[secpos]] = \
                    board2[posVert[secpos]][
                        posHori[secpos]], \
                    board2[posVert[frspos]][
                        posHori[frspos]]
                if not is_valid_move(posWK, board2):
                    print('incorrect path')
                    continue
        except (ValueError, KeyError): pass
    elif colorselect == 'Black' and count_move % 2 == 0: #and count_move % 2 == 0
        try:
            stockfish.set_fen_position(fen())
            if stockfish.get_best_move() == None:
                print('checkmate!')
                exit()
            ee = st()
            frspos, secpos = ee[:2], ee[3:5]
            print(frspos, secpos)
            if board[posVert[frspos]][posHori[frspos]] == BK:
                if not is_valid_move(secpos, board):
                    print('incorrect path')
                    continue
            elif colorBoard[posVert[frspos]][posHori[frspos]][0] != 'B':
                print('incorrect path')
                continue
            else:
                board2 = []
                for i in board:
                    mas = []
                    for j in i:
                        mas.append(j)
                    board2.append(mas)
                board2[posVert[secpos]][posHori[secpos]] = '..'
                board2[posVert[frspos]][posHori[frspos]], board2[posVert[secpos]][posHori[secpos]] = \
                board2[posVert[secpos]][
                    posHori[secpos]], \
                board2[posVert[frspos]][
                    posHori[frspos]]
                if not is_valid_move(posBK, board2):
                    print('incorrect path')
                    continue
        except (ValueError, KeyError): pass

    else:
        stockfish.set_fen_position(fen())
        try:
            move = stockfish.get_best_move().upper()
        except (AttributeError, IndexError):
            pass
            # print('checkmate!')
            # exit()
        frspos = move[:2]
        secpos = move[2:4]
        print(frspos, secpos)

    try:
        if board[posVert[frspos]][posHori[frspos]].check_move(frspos, secpos):

            if board[posVert[frspos]][posHori[frspos]] == WK:
                posWK = secpos
                flagWK = False
                flagK = False
                flagQ = False
            if board[posVert[frspos]][posHori[frspos]] == BK:
                posBK = secpos
                flagBK = False
                flagk = False
                flagq = False
            if board[posVert[frspos]][posHori[frspos]] == WL1:
                flagWL1 = False
                flagQ = False
            if board[posVert[frspos]][posHori[frspos]] == WL2:
                flagWL2 = False
                flagK = False
            if board[posVert[frspos]][posHori[frspos]] == BL1:
                flagBL1 = False
                flagq = False
            if board[posVert[frspos]][posHori[frspos]] == BL2:
                flagBL2 = False
                flagk = False
            movep2 = flagp2.upper()

            chess_move(frspos, secpos)

            flagpvz += 1
            flagp2 = '-'

        else:
            print('incorrect path')
    except:
        pass
