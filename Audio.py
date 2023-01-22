import vosk
import sys
import sounddevice as sd
import queue
import json
from fuzzywuzzy import fuzz

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
    print(voice)
    for i in range(len(vv)):
        if vv[i] == ' ':
            #print(v)
            conf(v)
            v = ''
        else:
            v += vv[i]



def conf(v: str):

    #A
    if v == "а":
        print("A")
    #B
    elif v == "бы" or v == "бэ" or v == "быт" or v == "бэт" or v == "бей" or v == "б" or v == "бэд":
        print("B")
    #C
    elif v == "це" or v == "со":
        print("C")
    #D
    elif v == "дэ" or v == "да" or v == "ты" or v == "дай":
        print("D")
    #E
    elif v == "е" or v == "я" or v == "ей" or v == "есть" or v == "зе" or v == "все":
        print("E")
    #F
    elif v == "эф" or v == "в":
        print("F")
    #G
    elif v == "джи" or v == "джим" or v == "джой" or v == "же":
        print("G")
    #H
    elif v == "аш" or v == "аж":
        print("G")

    #numbers
    elif v == 'один':
        print("1")
    elif v == "два":
        print("2")
    elif v == "три":
        print("3")
    elif v == "четыре":
        print("4")
    elif v == "пять":
        print("5")
    elif v == "шесть":
        print("6")
    elif v == "семь":
        print("7")
    elif v == "восемь":
        print("8")
    #specials
    elif v == "едва":
        print("E2")


va_listen(check)