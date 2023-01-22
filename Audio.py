import vosk
import sys
import sounddevice as sd
import queue
import json

model = vosk.Model("model-small_rus") #Write ur path

samplerate = 16000
device = 0

q = queue.Queue()


def q_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

rec = vosk.KaldiRecognizer(model, samplerate)


def va_listen(callback):
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device, dtype='int16',
                           channels=1, callback=q_callback):  #latency -- задержка?
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                callback(json.loads(rec.Result())["text"])




def check(voice: str):
    v = ''
    vv = voice + ' '
    gg = ''
    print(voice)
    for i in range(len(vv)):
        if vv[i] == ' ':
            #print(v)
            #print(conf(v))

            '''if conf(v) == 1 or conf(v) == 2 or conf(v) == 3 or conf(v) == 4 \
               or conf(v) == 5 or conf(v) == 6 or conf(v) == 7 or conf(v) == 8:
                gg += conf(v)
                gg += ' '
            else:'''
            if conf(v) == None:
                pass
            else:
                gg += conf(v)
            v = ''

        else:
            v += vv[i]

    print(gg[:2] + ' ' + gg[2:])
    gg = ''

    #print(gg)
    #gg.clear()




def conf(v: str):

    #A
    if v == "а":
        return("A")
    #B
    elif v == "бы" or v == "бэ" or v == "быт" or v == "бэт" or v == "бей" or v == "б" or v == "бэд":
        return("B")
    #C
    elif v == "це" or v == "со" or v == "цель":
        return("C")
    #D
    elif v == "дэ" or v == "да" or v == "ты" or v == "дай":
        return("D")
    #E
    elif v == "е" or v == "я" or v == "ей" or v == "есть" or v == "зе" or v == "все":
        return("E")
    #F
    elif v == "эф" or v == "в":
        return("F")
    #G
    elif v == "джи" or v == "джим" or v == "джой" or v == "же":
        return("G")
    #H
    elif v == "аш" or v == "аж":
        return("H")

    #numbers
    elif v == 'один':
        return("1")
    elif v == "два":
        return("2")
    elif v == "три":
        return("3")
    elif v == "четыре":
        return("4")
    elif v == "пять":
        return("5")
    elif v == "шесть":
        return("6")
    elif v == "семь":
        return("7")
    elif v == "восемь":
        return("8")
    #specials
    elif v == "едва":
        return("E2")

    else:
        pass


va_listen(check)
