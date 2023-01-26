import speech_recognition as sp
import time

#time.sleep(0.5)
print("start")

sr = sp.Recognizer()
sr.pause_threshold = 0.7
#sr.phrase_threshold = 0.2

with sp.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic, duration=0.5)
    audio = sr.listen(source=mic)
    query = sr.recognize_google(audio_data=audio, language='ru-Ru').lower()

print(query)
#print(sr.recognize_google.actual_result)